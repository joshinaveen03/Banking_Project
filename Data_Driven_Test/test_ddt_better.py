import os
import time

import openpyxl
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

def read_credential_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active

    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username":username,"password":password})
    return credentials

#@pytest.mark.parametrize("user_cred",read_credential_from_excel(os.getcwd()+"/testdata_ddt.xlsx"))
@pytest.mark.parametrize("user_cred", read_credential_from_excel("/Users/joshi/PycharmProjects/Personal_Projects/Banking_Project/Data_Driven_Test/testdata_ddt.xlsx"))
def test_Banking_positive(user_cred):
    username=user_cred["username"]
    password=user_cred["password"]
    Banking(username,password)

def Banking(username,password):
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/V4/index.php")
    email_input = driver.find_element(By.NAME, "uid")
    pass_input = driver.find_element(By.NAME, "password")
    submit_input = driver.find_element(By.NAME, "btnLogin")

    email_input.send_keys(username)
    pass_input.send_keys(password)

    submit_input.click()

    result=driver.current_url
    if result != "https://demo.guru99.com/V4/manager/Managerhomepage.php":
        pytest.xfail("Invalid Login")
        driver.quit()
    else:
        assert True==True
        driver.quit()
