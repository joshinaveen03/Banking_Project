#Page Locators
#Page Actions
#Web driver - Init
#Custom Fuction

from selenium.webdriver.common.by import By

class loginPage():
    def __init__(self,driver):
        self.driver=driver

    #Page Locator

    username=(By.XPATH,"//input[@name='uid']")
    password=(By.XPATH,"//input[@name='password']")
    submit=(By.XPATH,"//input[@name='btnLogin']")
    reset=(By.XPATH,"//input[@name='btnReset']")


    #Return a webelements -> username

    def get_username(self):
        return self.driver.find_element(*loginPage.username)

    def get_password(self):
        return self.driver.find_element(*loginPage.password)

    def get_submit(self):
        return self.driver.find_element(*loginPage.submit)

    def get_reset(self):
        return self.driver.find_element(*loginPage.reset)

    #Page Actions

    def login_to_banking(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit().click()

    def login_reset(self):
        self.get_reset().click()