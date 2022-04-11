import pytest
from selenium import webdriver


@pytest.fixture()

def setup(request):
    driver=webdriver.Chrome(executable_path="E:\\Driver\\chromedriver.exe")
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver=driver
    #Assigning the local driver to class driver
    yield
    driver.close
