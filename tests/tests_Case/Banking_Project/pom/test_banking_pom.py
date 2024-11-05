import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.loginPage import loginPage
from tests.pageObjects.dashboardPage import DashBoardPage
from tests.pageObjects.addCustomerPage import AddCustomerPage


class TestLogin():
    @allure.epic("Banking Login Test")
    @allure.feature("TC#0 - Banking Negative Test")
    @pytest.mark.usefixtures("setup")
    def test_banking_negative(self, setup):
        driver = setup
        LoginPage = loginPage(driver)
        LoginPage.login_to_banking(user="admin", pwd="123456")
        time.sleep(5)


    @allure.epic("Banking Login Test")
    @allure.feature("TC#1 - Banking Positive Test")
    @pytest.mark.usefixtures("setup")
    def test_banking_positive(self,setup):
        driver = setup
        LoginPage = loginPage(driver)
        LoginPage.login_to_banking(user=self.username, pwd=self.password)
        time.sleep(2)
        # Verify
        #assert "Welcome To Manager's Page of GTPL Bank"
        DashBoard=DashBoardPage(driver)
        homepage=DashBoard.get_homepage_text()
        assert homepage == "Welcome To Manager's Page of Guru99 Bank"
        print("Login successful, user is on the Manager's Dashboard.")
        time.sleep(2)

        dashboard_page = DashBoardPage(driver)
        dashboard_page.new_customer_click()

        AddCustomerDetails= AddCustomerPage(driver)
        addCustumerDetails = AddCustomerDetails.get_add_customer_text()
        assert addCustumerDetails == "Add New Customer"
        print("Login successful, Add Customer Details")
        time.sleep(2)









