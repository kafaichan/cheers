import pytesseract
import cv2
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'

def test(img_path):
	print(img_path)
	img = cv2.imread(img_path, 0)
	clean_img = cv2.medianBlur(img, 1)
	return pytesseract.image_to_string(Image.fromarray(clean_img), config="hex.txt")


if __name__ == "__main__":
	print(test('img/1.png'))