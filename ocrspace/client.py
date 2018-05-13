# Constants
ARABIC = "ara"
BULGARIAN = "bul"
CHINESE_SIMPLE = "chs"
CHINESE_TRADITIONAL = "cht"
CROATIAN = "hrv"
CZECH = "cze"
DANISH = "dan"
DUTCH = "dut"
ENGLISH = "eng"
FINNISH = "fin"
FRENCH = "fre"
GERMAN = "ger"
GREEK = "gre"
HUNGARIAN = "hun"
KOREAN = "kor"
ITALIAN = "ita"
JAPANESE = "jpn"
NORWEGIAN = "nor"
POLISH = "pol"
PORTUGUESE = "por"
RUSSIAN = "rus"
SLOVENIAN = "slv"
SPANISH = "spa"
SWEDISH = "swe"
TURKISH = "tur"


class Client:
    def __init__(self, api_key, language=ENGLISH, overlay=False, pdf=False, pdf_text_layer=True):
        self.api_key = api_key
        self.language = language
        self.overlay = overlay
        self.pdf = pdf
        self.pdf_text_layer = pdf_text_layer