import os



class Main:

    TEST_SERVER = os.getenv('TEST_SERVER', 'QA')

    ALL_SERVER_URLS = {'QA': 'http://automationpractice.com/'}
    ALL_USERS = {'QA_USER_EMAIL': 'sm_user@email.com', 'QA_USER_PASS': 'dave123johnes'}

    TEST_SERVER_URL = ALL_SERVER_URLS[TEST_SERVER]
    TEST_USER_EMAIL = ALL_USERS[TEST_SERVER + '_USER_EMAIL']
    TEST_USER_PASS = ALL_USERS[TEST_SERVER + '_USER_PASS']