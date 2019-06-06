import time
from selenium import webdriver
import random
from download_img import download, BASE_URL
from selenium.webdriver import ActionChains
from pyrobot import Robot, Keys
from ocr import test
import os
from config import Config


def run():
	driver = webdriver.Chrome(executable_path= os.path.join(os.getcwd(), "chromedriver_win32", "chromedriver.exe"))
	# driver.maximize_window()
	driver.get("https://eservice.macaotourism.gov.mo/tourist_tax_questionnaire/?lang=0")

	q0s = driver.find_elements_by_class_name("yes")
	q0s[0].click()
	time.sleep(1)

	q0s = driver.find_elements_by_class_name("yes")
	q0s[1].click()
	time.sleep(1)
	
	q1s = driver.find_element_by_xpath("//input[@name='a1']")
	q1s.click()
	time.sleep(1)

	for x in range(1,7):
		xpath = "//input[@name='a1_{}']".format(x)
		q1s_subq = driver.find_element_by_xpath(xpath)
		q1s_subq.click()
	
	q2 = driver.find_element_by_xpath("//input[@name='a2']")
	q2.click()

	q3 = driver.find_element_by_xpath("//input[@name='a3']")
	choices = [ str(x) for x in range(100, 600, 50)]
	q3.send_keys(random.choice(choices))
	
	for x in range(1, 7):
		xpath = "//input[@name='a4_{}']".format(x)
		q4_subq = driver.find_element_by_xpath(xpath)
		q4_subq.click()

	q5 = driver.find_elements_by_xpath("//input[@name='a5']")[4]
	q5.click()

	for x in range(1, 12):
		idx = random.choice([0,1])
		xpath = "//input[@name='a6_{}']".format(x)
		q6_subq = driver.find_elements_by_xpath(xpath)[idx]
		q6_subq.click()

	gender = random.randint(0,1)
	q7 = driver.find_elements_by_xpath("//input[@name='gender']")[gender]
	print(q7)
	q7.click()

	age = random.randint(0, 5)
	q8 = driver.find_elements_by_xpath("//input[@name='age']")[age]
	q8.click()

	occup = random.randint(0, 12)
	q9 = driver.find_elements_by_xpath("//input[@name='occupation']")[occup]
	q9.click()


	confirm_chkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")[-1]
	confirm_chkbox.click()

	try_count = 0
	success = False

	while not success:
		img = driver.find_element_by_id("captcha-image")
		# src = img.get_attribute('src')
		# download(src, "tmp.png")
		action_chains = ActionChains(driver)
		action_chains.context_click(img).perform()

		robot = Robot()
		robot.key_press("v")
		robot.key_release("v")
		time.sleep(2)
		robot.key_press(Keys.enter)
		robot.key_release(Keys.enter)
		time.sleep(4)


		# SET download_dir as the default download location of the pop up window
		img_path = os.path.join(Config.download_dir, "captcha_code.php")
		result = test(img_path)
		print("Captcha Code: ", result)

		if os.path.exists(img_path):
			os.remove(img_path)

		captcha_box = driver.find_element_by_xpath("//input[@name='captcha_code']")
		captcha_box.send_keys(result)
		time.sleep(1)

		submit_btn = driver.find_element_by_xpath("//input[@type='submit']")
		submit_btn.click()
		time.sleep(1)

		try:
			driver.find_element_by_xpath("//input[@name='captcha_code']")
			try_count += 1
		except:
			success = True

	driver.quit()

i = 0
while True:
	run()
	i += 1
	if i % 1000 == 0: print("Processed {} survey".format(i))
	time.sleep(1)
	