import img2pdf
from base64 import b64decode


def toPDF(self, file_name, list_of_base64=[]):
    list_of_base64 = [parse_base64(i) for i in list_of_base64]
    with open(f"{file_name}.pdf", "wb") as f:
        f.write(img2pdf.convert(list_of_base64))
    return f"{file_name}.pdf"


def parse_base64(string):
    if string.startswith("data:image"):
        return b64decode(string.split(",")[1], validate=True)
