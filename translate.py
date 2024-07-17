import json
from deep_translator import GoogleTranslator

class Translator:
    def __init__(self, source_language='nepali', target_language='english'):
        self.source_language = source_language
        self.target_language = target_language
        self.translator = GoogleTranslator(source=source_language, target=target_language)

    def chunk_text(self, text, chunk_size=500):
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def translate_text(self, input_text):
        chunks = self.chunk_text(input_text)
        translated_chunks = []
        for chunk in chunks:
            try:
                translation = self.translator.translate(chunk)
                translated_chunks.append(translation)
            except Exception as e:
                print(f"Translation failed for chunk: {chunk}. Error: {str(e)}")
                translated_chunks.append(chunk)  # Append original chunk if translation fails

        translated_text = ' '.join(translated_chunks)
        return translated_text

    def save_translated_text_to_txt(self, translated_text):
        output_txt_path = 'translated_text.txt'
        with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(translated_text)
        return output_txt_path

    def translate_json(self, input_file, output_file):
        with open(input_file) as i18n_file:
            parsed_json = json.load(i18n_file)

        translated_results = []
        for item in parsed_json:
            text = item['text']
            translated_text = self.translate_text(text)
            item['translated_text'] = translated_text
            translated_results.append(item)

        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(translated_results, output_file, ensure_ascii=False, indent=4)

        final_translated_text = ' '.join(item['translated_text'] for item in translated_results)
        translated_text_file = self.save_translated_text_to_txt(final_translated_text)
        return translated_text_file


if __name__=='__main__':
    text = 'मेरो नाम सागर सन्जय खनाल ह।  म इन्स्पिरिन्ग ल्याब मा काम गर्छ।'
    text1 = 'उन्मुक्तिको अध्यक्ष बनेका चौधरीको वैधानिकतामा प्रश्न'
    t= Translator()
    output = t.translate_text(text1)
    print(output)
