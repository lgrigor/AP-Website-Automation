from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Common_Page:
    def click(self, locator, timeout=3, poll_frequency=1):
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text, timeout=3, poll_frequency=1):
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator)).send_keys(text)