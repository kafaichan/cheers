import requests
import os
import shutil
import time

BASE_URL = "https://eservice.macaotourism.gov.mo/tourist_tax_questionnaire/captcha_code.php"


def download(img_url, img_path):
	with open(img_path, 'wb') as output_file,\
	requests.get(img_url, stream=True, verify=False) as response:
		shutil.copyfileobj(response.raw, output_file)


if __name__ == "__main__":

	if not os.path.exists("img"):
		os.makedirs("img")

	for x in range(100):
		img_url = BASE_URL
		img_path = os.path.join("img/{}.png".format(x))
		download(img_url, img_path)
		time.sleep(1)
