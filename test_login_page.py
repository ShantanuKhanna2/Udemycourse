from selenium.webdriver.common.by import By
class test_Login_page():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_name   = "dispatch[auth.login]"

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME,self.login_button_name).click()

