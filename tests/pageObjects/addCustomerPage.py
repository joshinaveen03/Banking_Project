#Page Locators
#Page Actions
#Web driver - Init
#Custom Fuction
import time

from selenium.webdriver.common.by import By

class AddCustomerPage():
    def __init__(self,driver):
        self.driver=driver
    #Locator
    addNewCustomerDetails=(By.XPATH,"//p[@class='heading3']")

    def get_add_customer(self):
        return self.driver.find_element(*AddCustomerPage.addNewCustomerDetails)

    def get_add_customer_text(self):
        return self.get_add_customer().text