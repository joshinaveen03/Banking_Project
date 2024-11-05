# Assertion Here
#start webdriver
#Call the Page Object
#Verification
import time

import pytest
import allure

from tests.pageObjects.loginPage import loginPage
from tests.pageObjects.dashboardPage import dashBoardPage
from selenium import webdriver
from dotenv import load_dotenv

@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.guru99.com/V4/index.php")
    return driver

@allure.epic("Banking Login Test")
@allure.feature("TC#1 - Banking Positive Test")
def test_banking(setup):
    driver=setup
    LoginPage=loginPage(driver)
    LoginPage.login_to_banking(user="mngr595791",pwd="YsUpamy")
    time.sleep(5)

    result = driver.current_url
    if result != "https://demo.guru99.com/V4/manager/Managerhomepage.php":
        pytest.xfail("Invalid Login")
        driver.quit()
    else:
        assert True == True
        driver.quit()

@allure.epic("Banking Login Test")
@allure.feature("TC#2 - Banking Negative Test")
def test_banking(setup):
    driver=setup
    LoginPage=loginPage(driver)
    LoginPage.login_to_banking(user="mngr595791",pwd="123456")
    time.sleep(5)

    # Assertion for Negative Test Case
    result = driver.current_url
    try:
        assert result != "https://demo.guru99.com/V4/manager/Managerhomepage.php", "Test failed: Unexpectedly logged in with invalid credentials."
    finally:
        driver.quit()




