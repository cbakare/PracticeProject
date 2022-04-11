from selenium.webdriver.common.by import By


class LandingPage:
    Amazon_SignIn_Account = (By.ID,"nav-link-accountList-nav-line-1")
    Amazon_sign_link = (By.CLASS_NAME,"nav-action-inner")

    def __init__(self,driver):
        self.driver=driver


    def LandingPageItems(self):
        return self.driver.find_element(*LandingPage.Amazon_SignIn_Account)

