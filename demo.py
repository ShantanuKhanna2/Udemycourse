from selenium import webdriver
import time
from POMDemo.Test_Pages.test_login_page import test_Login_page


driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
time.sleep(2)

login = test_Login_page(driver)
login.enter_username("shantanu.khanna1@shipway.in")
login.enter_password("Shaan@123")
login.click_login()
driver.refresh()
driver.find_element_by_xpath(
        "//body/div[@id='main_column']/div[1]/div[1]/div[1]/div[2]/ul[1]/li[8]/a[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Rate Card')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Rate Calculator')]").click()
driver.close()
driver.quit()