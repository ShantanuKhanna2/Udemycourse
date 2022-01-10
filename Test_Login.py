from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time
from POMDemo.Test_Pages.test_login_page import test_Login_page
from POMDemo.Test_Pages.test_order_assign import test_Order_Assign

class Test_Sample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        ser = Service(executable_path="C:/Users/Lenovo/PycharmProjects/Udemycourse/drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=ser)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test Completed")

    def test_login(self,test_setup):
        driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
        time.sleep(4)

        login = test_Login_page(driver)
        login.enter_username("shantanu.khanna1@shipway.in")
        login.enter_password("Shaan@123")
        login.click_login()

        assign = test_Order_Assign(driver)
        assign.click_quick_assign()
        time.sleep(4)
        assign.click_carrier_name()
        time.sleep(4)
        assign.click_assign_button()
        time.sleep(4)
        # driver.find_element(By.ID,"username").send_keys("shantanu.khanna1@shipway.in")
        # driver.find_element(By.ID,"password").send_keys("Shaan@123")
        # driver.find_element(By.NAME,"dispatch[auth.login]").click()
        # driver.find_element(By.ID,"quick_assign_15236265").click()
        # time.sleep(4)
        # driver.find_element(By.ID,"carrier_id_7377_15236265").click()
        # time.sleep(4)
        # driver.find_element(By.ID,"order_assign_button_15236265").click()
        # driver.close()
        # driver.quit()