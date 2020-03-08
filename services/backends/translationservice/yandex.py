import requests
import json
from django.conf import settings
from requests import Response
from typing import List, Dict


class Yandex:
    """Yandex translation engine - A backend for translation service"""

    # The following list of possible locales supported by Yandex API is obtained
    # by calling the API https://tech.yandex.com/translate/doc/dg/reference/getLangs-docpage/
    possible_locale_list: List[str] = [
        "af",
        "am",
        "ar",
        "az",
        "ba",
        "be",
        "bg",
        "bn",
        "bs",
        "ca",
        "ceb",
        "cs",
        "cv",
        "cy",
        "da",
        "de",
        "el",
        "en",
        "eo",
        "es",
        "et",
        "eu",
        "fa",
        "fi",
        "fr",
        "ga",
        "gd",
        "gl",
        "gu",
        "he",
        "hi",
        "hr",
        "ht",
        "hu",
        "hy",
        "id",
        "is",
        "it",
        "ja",
        "jv",
        "ka",
        "kk",
        "km",
        "kn",
        "ko",
        "ky",
        "la",
        "lb",
        "lo",
        "lt",
        "lv",
        "mg",
        "mhr",
        "mi",
        "mk",
        "ml",
        "mn",
        "mr",
        "mrj",
        "ms",
        "mt",
        "my",
        "ne",
        "nl",
        "no",
        "pa",
        "pap",
        "pl",
        "pt",
        "ro",
        "ru",
        "si",
        "sk",
        "sl",
        "sq",
        "sr",
        "su",
        "sv",
        "sw",
        "ta",
        "te",
        "tg",
        "th",
        "tl",
        "tr",
        "tt",
        "udm",
        "uk",
        "ur",
        "uz",
        "vi",
        "xh",
        "yi",
        "zh",
    ]

    def __init__(self):
        # Configure the Yandex API
        self.yandex_api_path: str = settings.YANDEX_API_PATH
        self.yandex_api_key: str = settings.YANDEX_API_KEY
        if not self.yandex_api_path:
            raise Exception("YANDEX_API_PATH can't be empty")
        if not self.yandex_api_key:
            raise Exception("YANDEX_API_KEY can't be empty")

    def translate(self, source: str, target: str, text: str) -> str:
        """Translate the given text from source locale to target"""

        request_url: str = "{0}?lang={1}-{2}&key={3}".format(
            self.yandex_api_path, source, target, self.yandex_api_key
        )

        response: Response = requests.post(url=request_url, data={"text": text})

        translated_text: str = ""
        if response.status_code == 200:
            response_data: Dict = response.json()
            translated_text: str = response_data.get("text")[0]
        return translated_text

    def validate_locale(self, locale: str) -> bool:
        """Validates if translation service supports this locale"""

        return locale in self.possible_locale_list

    def get_locales(self) -> List[str]:
        """Gets the list of supported locales"""

        return self.possible_locale_list


"""
The abbreviations refer to following languages
"langs": {
    "af": "Afrikaans",
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "cs": "Czech",
    "cv": "Chuvash",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "gd": "Scottish Gaelic",
    "gl": "Galician",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "ht": "Haitian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jv": "Javanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "ky": "Kyrgyz",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mhr": "Mari",
    "mi": "Maori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mr": "Marathi",
    "mrj": "Hill Mari",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pa": "Punjabi",
    "pap": "Papiamento",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "tl": "Tagalog",
    "tr": "Turkish",
    "tt": "Tatar",
    "udm": "Udmurt",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "zh": "Chinese"
}
"""
