class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    select = ("xpath", "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card")
    add = ("xpath", "/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button")
    submit = ("xpath", "//*[@id='navbarResponsive']/ul/li/a")
    checkout = ("xpath", "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button")
    country = ("id", "country")
    waiting = ("xpath", "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a")
    checkbox = ("xpath", "//*[@id='checkbox2']")

    def purchase(self):
        return self.driver.find_elements(*CheckOutPage.select)

    def clickProduct(self):
        return self.driver.find_element(*CheckOutPage.add)

    def submt(self):
        return self.driver.find_element(*CheckOutPage.submit)

    def check_out(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def enter_id(self):
        return self.driver.find_element(*CheckOutPage.country)

    #def checkboxes(self):
        #self.driver.find_element(*CheckOutPage.checkbox)
