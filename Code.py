from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import cv2
import pytesseract as pyte
import os
import shutil
import selenium.webdriver.support.ui as ui

fp = webdriver.FirefoxProfile("/home/shivasankaran/mzdir") # mzdir should be your profile directory
driver=webdriver.Firefox(fp)
driver.maximize_window()
driver.get('https://www.google.com?q=google.com#q=google.com')
first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')
for i in range(2):
    first_link.send_keys(Keys.CONTROL + Keys.RETURN)
first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('rc'))
driver.switch_to.window(driver.window_handles[1])
driver.get("https://storydownloader.net/")
driver.switch_to.window(driver.window_handles[2])
driver.get('https://www.google.com?q=ffreward#q=ffreward') # replace ffreward with anything that google search will give the redemption site as first result
first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')
for i in range(10):
    first_link.send_keys(Keys.CONTROL + Keys.RETURN)

driver.switch_to.window(driver.window_handles[1])
print("loaded storydownloader.net")
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("<username>")
print("Entering profile")
elem.send_keys(Keys.RETURN)
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'stories')))
elemxpath="//a[@class='btn btn-download' and @download=''] "
elem=driver.find_element_by_xpath(elemxpath)
elem.click()
print("Downloading latest video")
time.sleep(5)



video_name=os.listdir("/home/shivasankaran/insta_video")[0]
print(video_name)
video_path="/home/shivasankaran/insta_video/"+video_name
redeem_codes=[]
videoobj=cv2.VideoCapture(video_path)
success, image = videoobj.read()
print("converting video into a image")
cv2.imwrite("/home/shivasankaran/insta_image/latest_image.jpg", image) 
text=pyte.image_to_string("/home/shivasankaran/insta_image/latest_image.jpg")
print("image stored")
my_list=text.split("\n")
for word in my_list:
    if len(word)==12:
        redeem_codes.append(word)
print("redeem codes extracted:")
print(redeem_codes)


tabno=3
for redeem_code in redeem_codes: # to log in to redemption site using fb
    driver.switch_to.window(driver.window_handles[tabno])
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/span')))
    elem=driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/span')
    elem.click()
    tabno=tabno+1
tabno=3
for redeem_code in redeem_codes: # to input redeem codes in the site
    driver.switch_to.window(driver.window_handles[tabno])   
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'input_serial_1')))
    elem=driver.find_element_by_id('input_serial_1')
    elem.send_keys(redeem_code)
    print(redeem_code)
    elem=driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[1]/div[2]/div/button')
    elem.click()
    tabno=tabno+1
        


