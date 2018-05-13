from PIL import Image
from io import BytesIO

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

    def file(self, file_name, language=None, overlay=None, pdf=None, pdf_text_layer=None):
        # Opening image file.
        pil_img = Image(file_name)

        return self.pil(pil_img, language=language, overlay=overlay, pdf=pdf, pdf_text_layer=pdf_text_layer)

    def pil(self, pil_img, language=None, overlay=None, pdf=None, pdf_text_layer=None):
        # Converting to RGB.
        if not pil_img.mode.startswith("RGB"):
            img = pil_img.convert("RGB")

        # Removing alpha.
        if pil_img.mode == "RGBA":
            background = Image.new('RGBA', pil_img.size, (255, 255, 255))
            pil_img = Image.alpha_composite(background, pil_img)

        file = BytesIO()
        pil_img.save(file, "PNG")