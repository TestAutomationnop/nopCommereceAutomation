class Loginpage:
    txt_username_id = "Email"
    txt_password_id = "Password"
    btn_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def checklogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def checklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_link_text).click()
