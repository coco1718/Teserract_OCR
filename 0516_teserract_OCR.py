
# # https://www.youtube.com/watch?v=L8q-KCbXybc

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

a = Image.open('news.jpg')

result = pytesseract.image_to_string(a, lang = 'kor')

print(result)

#C:\Users\user\anaconda3\python.exe C:\Users\user\PycharmProjects\pythonProject\0516_teserract_OCR.py
#난 한국사람이야


#Process finished with exit code 0