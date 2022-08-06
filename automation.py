from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome(executable_path=r"D:\Python learning\chromedriver.exe")

print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


chrome_browser.implicitly_wait(2)
popup = chrome_browser.find_element(by=By.ID, value='at-cv-lightbox-close')
popup.click()


user_message = chrome_browser.find_element(by=By.ID, value="user-message")
user_message.clear()
user_message.send_keys('I am Varsha!!!!!!!')

time.sleep(2)
show_message_button = chrome_browser.find_element(by=By.CLASS_NAME, value='btn-default')
show_message_button.click()

output_message = chrome_browser.find_element(by=By.ID, value='display')
assert 'I am Varsha!!!!!!!' in output_message.text

time.sleep(6)
chrome_browser.close()