from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    alert1 = browser.switch_to.alert
    alert_text = alert1.text
    print(alert_text.split(': ')[-1])

finally:
    time.sleep(10)
    browser.quit()


