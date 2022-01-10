from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import time
from POMDemo.Test_Pages.test_login_page import test_Login_page
from POMDemo.Test_Pages.test_order_assign import test_Order_Assign

class TestSample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #global driver
        ser = Service(executable_path="C:/Users/Lenovo/PycharmProjects/Udemycourse/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
        time.sleep(2)

        login = test_Login_page(driver)
        login.enter_username("shantanu.khanna1@shipway.in")
        login.enter_password("Shaan@123")
        login.click_login()
        time.sleep(3)

        assign = test_Order_Assign(driver)
        assign.click_quick_assign()
        time.sleep(4)
        assign.click_carrier_name()
        time.sleep(4)
        assign.click_assign_button()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test_page Completed")
