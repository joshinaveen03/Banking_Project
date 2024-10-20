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

@pytest.mark.positive
def test_Banking_positive():
    file_path=os.getcwd()
    full_file_path=file_path+"/testdata_ddt.xlsx"
    credentials=read_credential_from_excel(full_file_path)

    for user_cred in credentials:
        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        Banking(username,password)

       # time.sleep(5)


def Banking(username,password):
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/V4/index.php")
    email_input = driver.find_element(By.NAME, "uid")
    pass_input = driver.find_element(By.NAME, "password")
    submit_input = driver.find_element(By.NAME, "btnLogin")

    email_input.send_keys(username)
    pass_input.send_keys(password)

    submit_input.click()

    driver.quit()
