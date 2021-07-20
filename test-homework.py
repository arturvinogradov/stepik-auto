from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))
x_element = browser.find_element_by_id('book')
x_element.click()

x = int(browser.find_element_by_id('input_value').text)
y = math.log(abs(12*math.sin(x)))

answer = browser.find_element_by_id('answer')
answer.send_keys(str(y))

x_element = browser.find_element_by_css_selector("[type='submit']")
x_element.click()
