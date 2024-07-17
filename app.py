from extract import PDFExtractor
from translate import Translator

def read_pdf(pdf_path):
    # Extract text from PDF
    extractor = PDFExtractor(language='nep+eng')
    extracted_content_path = extractor.extract_and_save_to_json(pdf_path)

    # Translate extracted content
    translator = Translator()
    translated_text_file = translator.translate_json(extracted_content_path, 'translated_file.json')

    return translated_text_file


pdf_path = 'your path of pdf'
read_pdf(pdf_path)

