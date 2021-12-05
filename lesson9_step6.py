import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    browser.find_element(By.XPATH, '//button[@type="submit"][@class="trollface btn btn-primary"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    y = calc(x_element)
    browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(y)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


finally:
    time.sleep(0)
    browser.quit()
