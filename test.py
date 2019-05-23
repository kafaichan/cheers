import os
import cv2
import glob
import random

def compare_pattern(token):
	for filepath in glob.glob("pattern/*.png"):
		pattern = cv2.imread(filepath, 0)
		diff = cv2.subtract(pattern, token)
		if cv2.countNonZero(diff) == 0:
			return filepath.split("\\")[1].split(".png")[0]
	return None

def compare_3_8(token):
	pat_3 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 0, 0, 0, 0, 0, 255, 0], [0, 0, 0, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 255, 0], [0, 0, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 0, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
	pat_8 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 255, 255, 255, 0, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 0, 255, 255, 255, 255, 0, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 255, 0, 0, 0, 0, 255, 0], [0, 0, 255, 255, 255, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

	if token.tolist() == pat_3:
		return "3"
	elif token.tolist() == pat_8:
		return "8"


def test(img_path):
	labels = ['a','b','c','d','e']
	labels += [str(x) for x in range(10)]
	result = ""

	x = 13
	y = 0
	h = 30
	w = 48

	origin_img = cv2.imread(img_path, 0)
	ret, thres2 = cv2.threshold(origin_img, 0, 255, cv2.THRESH_BINARY_INV)

	crop_img = thres2[y:y+h, x:x+w]
	# show_img(crop_img)

	for idx, i in enumerate(range(0, w, 8)):
		token = crop_img[y:y+h, i:i+8]
		pred = compare_pattern(token)
		if pred is not None:
			if pred == "3" or pred == "8":
				pred = compare_3_8(token)
			result += pred
		else:
			pred = random.choice(labels)

	return result

if __name__ == "__main__":
	# img1 = cv2.imread("pattern/2.png", 0)
	# img2 = cv2.imread("pattern/8.png", 0)
	# print(img1.tolist())
	# print("\n")
	# print(img1)
	# diff = cv2.subtract(img1, img2)
	# if cv2.countNonZero(diff) == 0:
	# 	print("Equal")
	# else:
	# 	print("Not equal")
	pass
	# for x in range(100):
	# 	img_path = os.path.join("img/{}.png".format(x))
	# 	print("Image {}, {}".format(x, test(img_path)))