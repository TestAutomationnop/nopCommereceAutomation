import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from ProdcutObject.LoginPage import Loginpage
from Utilities.readProperties import ReadConfig
from Utilities.custom_logger import LogGen


class Test_001_LoginPage:
    baseUrl = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_page_title(self):

        self.logger.info("************ test started*********************")

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\login_page.jpg")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\login_page.jpg")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login_test(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.password)
        self.lp.checklogin()
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerceadministration"

        if act_title == exp_title:
            assert True
            time.sleep(15)
            self.lp.checklogout()
            self.driver.save_screenshot(".\\Screenshots\\Homepage_login.jpg")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\Homepage_login.jpg")
            self.driver.close()
            assert False

        self.logger.info("************ test started*********************")
