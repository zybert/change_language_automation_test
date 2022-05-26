from selenium import webdriver
from selenium.webdriver.common.by import By
from assertion import *
import time

# Scenario: Changing the language of application to Arabic.

# Given: User is on page https://symptomate.com/pl/diagnosis
driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver.exe')
driver.get('https://symptomate.com/pl/diagnosis')

# When: User accept the cookies.
cookies_accept = driver.find_element(By.ID, "cky-btn-accept")
cookies_accept.click()

# And: User click on change language button.
change_language = driver.find_element(By.ID, "header-language-selector")
change_language.click()

# And: User click on Arabic language from the list.
arabic_language = driver.find_element(By.XPATH, "//*[text()='العربيّة']")
arabic_language.click()
expected_url = "https://symptomate.com/ar/diagnosis/0"

    # dynamic wait until page is load
for i in range(0, 10):
    time.sleep(0.5)
    if driver.current_url==expected_url:
        break;

# Then: The page should be in Arabic.
header_language = driver.find_element(By.XPATH, "//header//nav[1]").text
main_language = driver.find_element(By.CLASS_NAME, "ui-text").text
footer_language = driver.find_element(By.XPATH, "//footer//nav[1]/a[4]").text

assert (driver.current_url == expected_url), \
    "Url address is not correct. Expected: '" + expected_url + "' got '" + driver.current_url + "'"
assert_check_language(header_language, "ar")
assert_check_language(main_language, "ar")
assert_check_language(footer_language, "ar")

print("Test passed.")
