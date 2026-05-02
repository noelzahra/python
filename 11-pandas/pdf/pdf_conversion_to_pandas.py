import pandas as pd
import pdfplumber
from pdfplumber.utils import extract_text, get_bbox_overlap, obj_to_bbox
import tabulate

#Process pdf
def process_pdf(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    all_text = []

    #iterate through pdf pages
    for page in pdf.pages:
        filtered_page = page
        chars = filtered_page.chars
        for table in page.find_tables():
            first_table_char = page.crop(table.bbox).chars(0)
            filtered_page = filtered_page.filter(lambda obj:
                get_bbox_overlap(obj_to_bbox(obj), table.bbox) is None 
            )
            chars = filtered_page.chars
            df = pd.DataFrame(table.extract())
            df.columns = df.iloc[0]
            markdown = df.drop(0).to_markdown(index=False)
            chars.append(first_table_char | {"text : markdown"})
        page_text = extract_text(chars, layout=True)
        all_text.append(page_text)
    pdf.close()
    return "\n".join(all_text)

pdf_path = r"python/11-pandas/pdf/sample.pdf"
extracted_text = process_pdf(pdf_path)
print(extracted_text)