from utils import path
from base64 import b64decode
import img2pdf
import os


def parse_base64(string):
    if string.startswith("data:image"):
        return b64decode(string.split(",")[1], validate=True)


def toPDF(file_name, list_of_base64=[]):
    list_of_base64 = [parse_base64(i) for i in list_of_base64]
    with open(os.path.join(path, file_name), "wb") as f:
        f.write(img2pdf.convert(list_of_base64))
    return f"{file_name}.pdf"
