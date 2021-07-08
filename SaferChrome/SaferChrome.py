import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

print('=====================================================================================================')
print('Loading proxy lists, Please Wait')
print('=====================================================================================================')
time.sleep(3)
print('Running chrome.exe')
time.sleep(4)

options = webdriver.ChromeOptions()
bot = webdriver.Chrome(options=options,  executable_path=CM().install())
bot.set_window_size(1680, 900)

bot.get('https://google.com/')
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
time.sleep(3)


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True

time.sleep(1000)
