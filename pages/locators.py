from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_RPASS = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    PRODUCT_ADDTOCARTBUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_ALERT_NAME = (
    By.XPATH, '(//div[@class="alert alert-safe alert-noicon alert-success  fade in"]/div/strong)[1]')
    PRODUCT_ALERT_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    PRODUCT_CART_PRICE = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]')
