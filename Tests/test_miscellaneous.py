import os
import sys

sys.path.append(sys.path[0] + '\\..')

from Resource.Common.tools import Tools
from Resource.main import Main
from Resource.Pages.common_page import Common_Page
from Resource.Pages.login_page import Login_Page
from Resource.Pages.main_page import Main_Page

EXPECTED_USER_PAGE = 'Resource\\Data\\n01_expected_user_page.png'


class TestSteps(Common_Page):
    def load_main_page(self, driver_setup):
        """Test Step 1: Open browser and load the provided URL"""
        self.driver = driver_setup
        self.driver.get(Main.TEST_SERVER_URL)

    def click_on_sign_in_button(self):
        """Test Step 2: Click on a sign in button"""
        self.click(Main_Page.SIGN_IN_BTN)

    def log_in_with_user_account(self):
        """Test Step 3: Fill user email and password on the appropriate fields"""
        self.input_text(Login_Page.EMAIL_ADDRESS_FLD, Main.TEST_USER_EMAIL)
        self.input_text(Login_Page.PASSWORD_FLD, Main.TEST_USER_PASS)
        self.click(Login_Page.SIGN_IN_BTN)

    def user_page_should_be_opened(self):
        """Test Step 4: Verify that user page was successfully opened"""
        ACTUAL_USER_PAGE = f'{os.environ["testlog"]}\\actual_user_page.png'
        self.driver.save_screenshot(ACTUAL_USER_PAGE)
        Tools.diffutil(ACTUAL_USER_PAGE, EXPECTED_USER_PAGE)


class Test_Suite_N01_TMPT1_2134(TestSteps):
    def test_case_N01_logging_in_with_happy_path(self, driver_setup):
        self.load_main_page(driver_setup)
        self.click_on_sign_in_button()
        self.log_in_with_user_account()
        self.user_page_should_be_opened()
