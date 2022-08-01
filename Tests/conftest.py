import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_setup(request):
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=3')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=3).install()), options=options)

    testname = request.node.name
    testlog = f'Results\\{testname}'

    os.environ['testlog'] = testlog
    
    if os.path.isdir(testlog):
        os.system(f'rm -rf {testlog}')

    os.makedirs(testlog)

    yield driver

    driver.close()

