class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = ("xpath", "/html/body/app-root/app-navbar/div/nav/ul/li[2]/a")
    names = ("xpath", "/html/body/app-root/form-comp/div/form/div[1]/input")
    email = ("xpath", "/html/body/app-root/form-comp/div/form/div[2]/input")
    password1 = ("xpath", "//*[@id='exampleInputPassword1']")
    checkbox = ("xpath", "//*[@id='exampleCheck1']")
    find = ("xpath", "//*[@id='exampleFormControlSelect1']")
    status = ("id", "inlineRadio2")
    sbmt = ("xpath", "/html/body/app-root/form-comp/div/form/input")
    succes = ("xpath", "/html/body/app-root/form-comp/div/div[2]/div")

    ########################################################################################################################
    #Below code is for checkout E2E flow
    def myShop(self):
        return self.driver.find_element(*HomePage.shop)

    ########################################################################################################################
    #Below code is for Sign in Page
    def name(self):
        return self.driver.find_element(*HomePage.names)

    def mail(self):
        return self.driver.find_element(*HomePage.email)

    def password(self):
        return self.driver.find_element(*HomePage.password1)

    def chekbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    #def finddropdown(self):
        #return self.driver.find_element(*HomePage.find)

    def empstatus(self):
        return self.driver.find_element(*HomePage.status)

    def submit(self):
        return self.driver.find_element(*HomePage.sbmt)

    def success(self):
        return self.driver.find_element(*HomePage.succes)
