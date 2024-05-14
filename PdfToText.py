import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python PdfToText.py <PDF_file>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    extracted_text = extract_text_from_pdf(pdf_file)
    
    # Write the transcribed text to a file
    output_file = "Parsing text from PDF.txt"
    with open(output_file, 'w') as output:
        output.write(extracted_text)

    print(f"Extracted text has been written to '{output_file}'")
