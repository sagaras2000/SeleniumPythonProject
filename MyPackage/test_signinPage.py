import pytest
from selenium import webdriver

from PageObject.HomePage import HomePage
from Utilities.BaseClass import MyClass


class TestLogin(MyClass):

    def test_Signin(self):
        log = self.myLogging()
        signin = HomePage(self.driver)
        signin.name().send_keys("Sagar S")
        signin.mail().send_keys("sas123@gmail.com")
        signin.password().send_keys("Pass123")
        log.info("Username/ Password and email has been sent")
        signin.chekbox().click()
        #signin.finddropdown()
        self.select_dropdown(num=0)
        signin.empstatus().click()

        signin.submit().click()
        success_message = signin.success().text
        assert ("success" in success_message)
        log.info(success_message)

    @pytest.fixture(params=[("sagar", "sas@gmail.com", "Pass123"), ("Vidhi", "vidhi@gmail.com", "pass123")])
    def getData(self, request):
        return request.param
