"""
ISCO coding module for natural language processing tasks using spaCy.
Maltese words are excluded.
"""

import os
import warnings
import pandas as pd
from pathlib import Path
import spacy
from huggingface_hub import snapshot_download
from langdetect import detect, LangDetectException, DetectorFactory
from transformers import MarianMTModel, MarianTokenizer

os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
DetectorFactory.seed = 0  # reproducible language detection

# Download (or reuse cached) spaCy model from HuggingFace Hub and load.
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    _model_path = snapshot_download("spacy/en_core_web_sm", ignore_patterns=["*.whl"])
nlp = spacy.load(_model_path)

# Load Maltese-to-English translation model from HuggingFace Hub.
_mt_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-mt-en")
_mt_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-mt-en")

#Create Dataframes for extract and ISCO codes
df = pd.read_excel(Path(__file__).parents[1] / "pandas/nlp.xlsx", index_col=False)
df_isco_codes = pd.read_excel(Path(__file__).parents[1] / "pandas/ISCO_codes.xlsx", index_col=False)

df_isco = df[["ID", "ICTSurvey.SectionI.I9_A", "ICTSurvey.SectionI.I9_B"]].dropna(
    subset=["ICTSurvey.SectionI.I9_A", "ICTSurvey.SectionI.I9_B"]
).reset_index(drop=True)

#Translate Maltese text to English.
def translate_to_english(text: str) -> str:
    try:
        if detect(text) == "mt":
            tokens = _mt_tokenizer([text], return_tensors="pt", padding=True)
            translated = _mt_model.generate(**tokens)
            return _mt_tokenizer.decode(translated[0], skip_special_tokens=True)
    except LangDetectException:
        pass
    return text


# Lemmatize and filter text to extract keywords for matching. Stripping stop words and punctuation for cleaner matching.
def extract_keywords(text: str) -> set[str]:
    doc = nlp(str(text).lower())
    return {token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha}


# Pre-process all ISCO titles into keyword sets for fast matching.
def build_isco_index(df_codes: pd.DataFrame) -> list[tuple[int, set[str]]]:
    index = []
    for _, row in df_codes.iterrows():
        keywords = extract_keywords(row["English title"])
        index.append((row["Isco-08"], keywords))
    return index

# Return best-matching Isco-08 code and Jaccard score for a free-text job description.
def match_isco_code(job_text: str, isco_index: list[tuple[int, set[str]]]) -> tuple[int | None, float | None]:
    job_keywords = extract_keywords(job_text)
    if not job_keywords:
        return None, None

    best_score = -1.0
    best_code = None

    for code, title_keywords in isco_index:
        union = job_keywords | title_keywords
        if not union:
            continue
        score = len(job_keywords & title_keywords) / len(union)
        if score > best_score:
            best_score = score
            best_code = code

    if best_score > 0:
        return best_code, round(best_score, 4)
    return None, None


def main():
    print("Building ISCO keyword index...")
    isco_index = build_isco_index(df_isco_codes)

    print(f"Matching {len(df_isco)} job descriptions to ISCO codes...")
    results = df_isco.apply(
        lambda row: match_isco_code(
            translate_to_english(
                str(row["ICTSurvey.SectionI.I9_A"]) + " " + str(row["ICTSurvey.SectionI.I9_B"])
            ),
            isco_index,
        ),
        axis=1,
    )
    df_isco["Isco-08"] = results.apply(lambda r: r[0])
    df_isco["Jaccard_score"] = results.apply(lambda r: r[1])

    output_path = Path(__file__).parent / "isco_output.xlsx"
    df_isco.to_excel(output_path, index=False)
    print(f"Saved to {output_path}")
    print(df_isco[["ICTSurvey.SectionI.I9_A", "ICTSurvey.SectionI.I9_B", "Isco-08", "Jaccard_score"]].head(20))


if __name__ == "__main__":
    main()
