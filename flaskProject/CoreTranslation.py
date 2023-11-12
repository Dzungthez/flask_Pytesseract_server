import html
import urllib

import aiohttp
import requests
import unicodedata
import logging

class TranslateManager:
    @staticmethod
    async def translate_word(text_to_translate, source_language, target_language):
        logging.debug(f"Text to translate: {text_to_translate}")
        # encoded_text = urllib.parse.quote(text_to_translate)
        # logging.debug(f"Encoded text: {encoded_text}")
        # encoded_text = requests.utils.quote(text_to_translate)
        api_url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language}&tl={target_language}&dt=t&text={text_to_translate}&op=translate"

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                translation_data = await response.json()
        logging.debug(f"Translation data: {translation_data[0][0][0]}")
        return await TranslateManager.parse_translation_response(translation_data)

    @staticmethod
    async def parse_translation_response(response):
        try:
            translation_segments = response[0]
            translated_text = "".join(segment[0] for segment in translation_segments)
            decoded_text = html.unescape(translated_text)
            normalized_text = unicodedata.normalize('NFKC', decoded_text)
            return normalized_text
        except (KeyError, IndexError):
            return ""

# import requests
# from urllib.parse import urlencode
# class TranslateManager:
#     GOOGLE_TRANSLATE_URL = "https://translate.google.com/translate_a/t?"
#
#     @staticmethod
#     async def translate_word(self,  text_to_translate, source_language, target_language):
#         url = self.generate_url(source_language, target_language, text_to_translate)
#         response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#         translated_text = response.text.strip().replace("\"", "").replace("[", "").replace("]", "")
#         return translated_text
#
#     @staticmethod
#     def generate_url(self, source_language, target_language, text):
#         params = {
#             "client": "gtrans",
#             "sl": source_language,
#             "tl": target_language,
#             "hl": target_language,
#             "q": text
#         }
#         url = self.GOOGLE_TRANSLATE_URL + urlencode(params)
#         return url
#
