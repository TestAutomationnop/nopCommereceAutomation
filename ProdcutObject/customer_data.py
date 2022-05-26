import time


class Customer_data:
    link_customer_menu_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    link_customer_menu_item_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[" \
                                    "1]/a[1]/p[1] "
    btn_add_new_xpath = "//a[@class='btn btn-primary']"
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_first_name_xpath = "//input[@id='FirstName']"
    text_last_name_xpath = "//input[@id='LastName']"
    rb_gender_male_xpath = "//label[contains(text(),'Male')]"
    rb_gender_female_xpath = "//label[contains(text(),'Female')]"
    text_dob_xpath = "//input[@id='DateOfBirth']"
    text_company_name_xpath = "//input[@id='Company']"
    cb_tax_exampt_xpath = "//input[@id='IsTaxExempt']"
    lb_role_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[" \
                    "2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lb_role_Admin_xpath = "//li[contains(text(),'Administrators')]"
    lb_role_register_xpath = "//li[contains(text(),'Registered')]"
    lb_role_vendor_xpath = "//li[contains(text(),'Vendors')]"
    lb_role_guest_xpath = "//li[contains(text(),'Guests')]"
    db_manage_vendor_xpath = "//select[@id='VendorId']"
    db_manage_vendor_vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    db_manage_vendor_vendor2_xpath = "//option[contains(text(),'Vendor 2')]"
    text_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    text_data_validation = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def get_customer_menu(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def get_customer_menu_list(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_item_xpath).click()

    def click_Add_customer(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()

    def get_email(self, email):
        self.driver.find_element_by_xpath(self.text_email_xpath).clear()
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys(email)

    def get_password(self, user_password):
        self.driver.find_element_by_xpath(self.text_password_xpath).clear()
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(user_password)

    def get_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.text_first_name_xpath).clear()
        self.driver.find_element_by_xpath(self.text_first_name_xpath).send_keys(first_name)

    def get_last_name(self, last_name):
        self.driver.find_element_by_xpath(self.text_last_name_xpath).clear()
        self.driver.find_element_by_xpath(self.text_last_name_xpath).send_keys(last_name)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rb_gender_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rb_gender_female_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rb_gender_male_xpath).click()

    def get_dob(self, dob):
        self.driver.find_element_by_xpath(self.text_dob_xpath).clear()
        self.driver.find_element_by_xpath(self.text_dob_xpath).send_keys(dob)

    def get_company_name(self, c_name):
        self.driver.find_element_by_xpath(self.text_company_name_xpath).clear()
        self.driver.find_element_by_xpath(self.text_company_name_xpath).send_keys(c_name)

    def tax_exampt(self):
        self.driver.find_element_by_xpath(self.cb_tax_exampt_xpath).click()

    def customer_role(self, role):

        self.driver.find_element_by_xpath(self.lb_role_xpath).click()
        time.sleep(5)

        if role == "Registerd":
            self.list_item = self.driver.find_element_by_xpath(self.lb_role_register_xpath)
        elif role == "Vendors":
            self.list_item = self.driver.find_element_by_xpath(self.lb_role_vendor_xpath)
        elif role == "Administrators":
            self.list_item = self.driver.find_element_by_xpath(self.lb_role_Admin_xpath)

        elif role == "Guests":
            time.sleep(5)
            self.list_item = self.driver.find_element_by_xpath(self.lb_role_guest_xpath)
        else:
            time.sleep(5)
            self.list_item = self.driver.find_element_by_xpath(self.lb_role_register_xpath)

        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def manage_vendor(self, value):
        self.driver.find_element_by_xpath(self.db_manage_vendor_xpath).click()
        time.sleep(3)
        if value == "Vendor 1":
            self.driver.find_element_by_xpath(self.db_manage_vendor_vendor1_xpath).click()
        elif value == "Vendor 2":
            self.driver.find_element_by_xpath(self.db_manage_vendor_vendor2_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.db_manage_vendor_vendor1_xpath).click()

    def admin_content(self, content):
        self.driver.find_element_by_xpath(self.text_admin_comment_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    def validation_user(self):
        self.msg = self.driver.find_element_by_xpath(self.text_data_validation)
        self.data = self.msg.get_attribute("innerHTML")
        return self.data

