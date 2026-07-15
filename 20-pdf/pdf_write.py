"""
Read and write PDF files
"""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject


def replace_text_in_pdf(input_path: str, output_path: str, old_text: str, new_text: str) -> None:
    reader = PdfReader(input_path)
    writer = PdfWriter()

    old_bytes = old_text.encode("utf-8")
    new_bytes = new_text.encode("utf-8")

    for page in reader.pages:
        contents = page.get("/Contents")
        if contents is not None:
            obj = contents.get_object()
            if isinstance(obj, ArrayObject):
                for stream_ref in obj:
                    stream_obj = stream_ref.get_object()
                    data = stream_obj.get_data()
                    stream_obj.set_data(data.replace(old_bytes, new_bytes))
            else:
                data = obj.get_data()
                obj.set_data(data.replace(old_bytes, new_bytes))
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

def main():
    input_pdf = "5837 letter.pdf"
    output_pdf = "5837 letter_edited.pdf"
    # Á is Unicode U+00C1, which encodes to byte 0xC1 in Latin-1 — matching the raw PDF stream
    old_text = "FERNÁNDEZ"
    new_text = "FERNANDEZ"

    replace_text_in_pdf(input_pdf, output_pdf, old_text, new_text)
    print(f"Saved '{output_pdf}' with '{old_text}' replaced by '{new_text}'.")

if __name__ == "__main__":
    main()
