from PIL import Image
import pytesseract

"""
After doing 'pip install pytesseract' command on windows cmd,
download and install tesseract file to do ocr.

The install file 'tesseract-ocr-w32-setup-v5.0.0-alpha.20200328'
is in 'Install File' directory.

Download Link:
https://github.com/UB-Mannheim/tesseract/wiki

How to use after installation:
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

After installing, Set the tesseract path in the script before
calling image_to_string:
pytesseract.pytesseract.tesseract_cmd = 
r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' #(the tesseract installation path)
"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r'F:\mohsen\POKER\Softwares\Installed programs\DeepMind Pokerbot\tesseract.exe'

im = Image.open("phototest.TIF")
text = pytesseract.image_to_string(im, lang = 'eng')
print(text)