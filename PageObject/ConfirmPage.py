

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    finalCheckout = ("xpath", "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")
    successid = ("xpath", "/html/body/app-root/app-shop/div/app-checkout/div/form/input")
    successmsg = ("xpath", "/html/body/app-root/app-shop/div/app-checkout/div[2]/div")


    def final_checkout(self):
        return self.driver.find_element(*ConfirmPage.finalCheckout)

    def success_id(self):
        return self.driver.find_element(*ConfirmPage.successid)

    def success_msg(self):
        return self.driver.find_element(*ConfirmPage.successmsg)
