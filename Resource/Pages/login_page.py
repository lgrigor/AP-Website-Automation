from selenium.webdriver.common.by import By



class Login_Page:
    EMAIL_ADDRESS_FLD = (By.XPATH, '//input[@id="email"]')
    PASSWORD_FLD = (By.XPATH, '//input[@id="passwd"]')
    SIGN_IN_BTN = (By.XPATH, '//button[@id="SubmitLogin"]')