import cv2
import os


def show_img(img):
	cv2.imshow("img", img)
	cv2.waitKey(0)

def split_img(img_path, img_id):
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
		# show_img(token)
		cv2.imwrite("split_result/{}_part{}.png".format(img_id, idx), token)


if __name__ == "__main__":
	if not os.path.exists("split_result"):
		os.makedirs("split_result")

	for x in range(100):
		img_path = os.path.join("img/{}.png".format(x))
		split_img(img_path, x)