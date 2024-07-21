import inspect
import pytest
import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


#######################################################################################################################
#This code is for E2E checkout
@pytest.mark.usefixtures("invokeBrowser")
class MyClass:
    def myLogging(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)

        handling = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        handling.setFormatter(formatter)

        logger.addHandler(handling)
        logger.setLevel(logging.DEBUG)
        return logger

    def presenseoflink(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            ("xpath", "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")))

    #######################################################################################################################
    #This code is for E2E checkout
    def select_dropdown(self, num):
        dropdown = Select(self.driver.find_element("id", "exampleFormControlSelect1"))
        dropdown.select_by_index(num)
