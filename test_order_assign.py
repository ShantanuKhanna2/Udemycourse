from selenium.webdriver.common.by import By
class test_Order_Assign():

    def __init__(self, driver):
        self.driver = driver

        self.quick_assign_id = "quick_assign_15441381"
        self.carrier_name_id = "carrier_id_7377_15441381"
        self.assign_button_id = "order_assign_button_15441381"

    def click_quick_assign(self):
        self.driver.find_element(By.ID,self.quick_assign_id).click()

    def click_carrier_name(self):
        self.driver.find_element(By.ID,self.carrier_name_id).click()

    def click_assign_button(self):
        self.driver.find_element(By.ID,self.assign_button_id).click()