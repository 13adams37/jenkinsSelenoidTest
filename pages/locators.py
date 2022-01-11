from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_RPASS = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
