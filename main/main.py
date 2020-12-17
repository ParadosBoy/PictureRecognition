from PIL import Image

import pytesseract

images = Image.open(r"C:\Users\10574\Desktop\1.png")
Chinese_sim = pytesseract.image_to_string(images,lang="chi_sim")
Chinese_tra = pytesseract.image_to_string(images,lang="chi_tra")
Japanese = pytesseract.image_to_string(images,lang="jpn")
Korean = pytesseract.image_to_string(images,lang="kor")
print(Korean)
