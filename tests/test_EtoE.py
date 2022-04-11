import pytest

from PageObjects.LandingPage import LandingPage
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_Loginpage(self):
        landingPage=LandingPage(self.driver)
        landingPage.LandingPageItems().click()
        loginPage=LoginPage(self.driver)
        Sign_in=loginPage.LoginPageItems()
        print(Sign_in.text)