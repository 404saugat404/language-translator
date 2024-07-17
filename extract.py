from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import json
import logging

logging.basicConfig(level=logging.INFO)

class PDFExtractor:
    def __init__(self, language='nep+eng'):
        self.language = language

    def extract_text_from_pdf(self, pdf_path):
        pdf_document = Document(document_path=pdf_path, language=self.language)
        pdf2text = PDF2Text(document=pdf_document)
        content = pdf2text.extract()

        output_json_path = 'extracted_content.json'
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(content, json_file, ensure_ascii=False, indent=4)
        
        return output_json_path

    def extract_and_save_to_json(self, pdf_path):
        extracted_content_path = self.extract_text_from_pdf(pdf_path)
        return extracted_content_path
