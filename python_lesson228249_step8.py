import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
with open("test.txt", "w") as file:
    content = file.write("automationbypython")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Sanya")
    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Petrov")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("sanya@petrov.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")
    send_file = browser.find_element(By.ID, "file")
    send_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

