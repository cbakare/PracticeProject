from selenium.webdriver.common.by import By


class LoginPage:

    Login_Sign_text=(By.CLASS_NAME,"a-spacing-small")

    def __init__(self,driver):
        self.driver=driver

    def Login_Page_items(self):
        return self.driver.find_element(*LoginPage.Login_Sign_text)

