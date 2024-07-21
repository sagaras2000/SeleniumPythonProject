
from Utilities.BaseClass import MyClass
from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from PageObject.CheckOutPage import CheckOutPage


class TestSelenium(MyClass):

    def test_RunScenario(self, invokeBrowser):
        log = self.myLogging()
        shoppage = HomePage(self.driver)
        shoppage.myShop().click()
        log.info("Get the Product details")
        checkout = CheckOutPage(self.driver)
        products = checkout.purchase()
        for i in products:
            log.info(i.text)
            if "Samsung" in i.text:
                checkout.clickProduct().click()
        checkout.submt().click()
        checkout.check_out().click()
        checkout.enter_id().send_keys("India")
        self.presenseoflink()
        confirm = ConfirmPage(self.driver)
        log.info("User is all set to checkout the product")
        confirm.final_checkout().click()
        #checkout.checkboxes().click()
        confirm.success_id().click()
        successful = confirm.success_msg().text
        log.info(successful)
