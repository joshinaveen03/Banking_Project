import pytest
from selenium import webdriver
from dotenv import load_dotenv

import os
load_dotenv()

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()


    username=os.getenv("Name")
    password=os.getenv("PASSWORD")
    base_url=os.getenv("BASE_URL")

    driver.get(base_url)

    request.cls.driver=driver
    request.cls.username=username
    request.cls.password=password
    request.cls.base_url=base_url

    yield driver
    driver.quit()
