import random
import string
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.custom_logger import LogGen
from Utilities.readProperties import ReadConfig
from ProdcutObject.LoginPage import Loginpage
from ProdcutObject.customer_data import Customer_data


def random_generator(size=8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(size))


class Test_002_customer_data:
    baseUrl = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_customer_data(self):
        self.logger.info("*********** test_002_customer_data started ********************* ")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.password)
        self.lp.checklogin()
        self.logger.info("*********** login done successfully ********************* ")

        self.logger.info("*********** customer data starting  ********************* ")

        self.add_cus = Customer_data(self.driver)
        time.sleep(15)
        self.add_cus.get_customer_menu()
        time.sleep(3)
        self.add_cus.get_customer_menu_list()
        time.sleep(5)
        self.add_cus.click_Add_customer()

        self.logger.info("*********** adding data to customer  ********************* ")

        self.email = random_generator() + "@gmail.com"

        self.add_cus.get_email(self.email)
        self.add_cus.get_password("Achala$123")
        self.add_cus.get_first_name("Achala")
        self.add_cus.get_last_name("Testing")
        self.add_cus.select_gender("Male")
        self.add_cus.get_dob("9/25/1996")
        self.add_cus.get_company_name("Achala it solutions")
        self.add_cus.tax_exampt()
        self.add_cus.customer_role("Vendors")
        self.add_cus.manage_vendor("Vendor 2")
        self.add_cus.admin_content("testing automation")
        time.sleep(3)
        self.add_cus.click_on_save()
        time.sleep(6)

        self.logger.info("*********** adding data to customer completed ********************* ")

        self.logger.info("*********** adding customer validation  ********************* ")

        self.content = self.add_cus.validation_user()
        print(self.content)

        if "The new customer has been added successfully." in self.content:
            assert True == True
            self.logger.info("*********** adding customer pass  ********************* ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\Add_customer_failed.jpg")
            self.logger.info("*********** adding customer Failed  ********************* ")
            assert True == False

        self.driver.close()
        self.logger.info("*********** adding customer Ended  ********************* ")
