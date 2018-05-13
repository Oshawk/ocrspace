from .response import Response
from io import BytesIO
from PIL import Image
from requests import post

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
        pil_img = Image.open(file_name)

        return self.pil(pil_img, language=language, overlay=overlay, pdf=pdf, pdf_text_layer=pdf_text_layer)

    def pil(self, pil_img, language=None, overlay=None, pdf=None, pdf_text_layer=None):
        # Converting to RGB.
        if not pil_img.mode.startswith("RGB"):
            pil_img = pil_img.convert("RGB")

        # Removing alpha.
        if pil_img.mode == "RGBA":
            background = Image.new('RGBA', pil_img.size, (255, 255, 255))
            pil_img = Image.alpha_composite(background, pil_img)

        # Creating file object in memory and saving the file as a PNG to it.
        file = BytesIO()
        pil_img.save(file, format="PNG")
        file.seek(0)

        # Applying initial data.
        data = {
            "apikey": self.api_key,
            "language": self.language,
            "isOverlayRequired": self.overlay,
            "isCreateSearchablePdf": self.pdf,
            "isSearchablePdfHideTextLayer": not self.pdf_text_layer
        }

        # Checking for and applying any overrides.
        if language is not None:
            data["language"] = language
        if overlay is not None:
            data["isOverlayRequired"] = overlay
        if pdf is not None:
            data["isCreateSearchablePdf"] = pdf
        if pdf_text_layer is not None:
            data["isSearchablePdfHideTextLayer"] = not pdf_text_layer

        response = post("https://api.ocr.space/parse/image", data=data, files={".png": file}).json()

        # Checking for an error.
        if isinstance(response, str):
            raise Exception(f"An error occurred. Message: {response}")

        return Response(response)
