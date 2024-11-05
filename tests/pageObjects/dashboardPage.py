#Page Locators
#Page Actions
#Web driver - Init
#Custom Fuction
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DashBoardPage():
    def __init__(self,driver):
        self.driver=driver
    #Locator
    user_homepage=(By.XPATH,"//marquee[@class='heading3']")
    new_customer=(By.XPATH,"//a[normalize-space()='New Customer']")


    #Web Element
    def get_homepage(self):
        return self.driver.find_element(*DashBoardPage.user_homepage)

    def new_customer_click(self):
        time.sleep(3)
        self.driver.find_element(*DashBoardPage.new_customer).click()

    #Page Action
    def get_homepage_text(self):
        return self.get_homepage().text








