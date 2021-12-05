import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
cash = "$100"
browser = webdriver.Chrome()
browser.implicitly_wait(5)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), cash)
    )
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    browser.close()
