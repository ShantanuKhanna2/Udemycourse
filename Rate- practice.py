import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

import Pincode_data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from POMDemo.Test_Pages.test_login_page import test_Login_page

ser = Service(executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(service= ser)

driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.maximize_window()

path ="../POMDemo/Pincodes.xlsx"

row = Pincode_data.getRowCount(path, "Sheet1")
column = Pincode_data.getColumnCount(path, "Sheet1")

# we will use this in case of print any particular locators
# def is_element_present(how,what):
#     if len(driver.find_element(by=how, value=what)) == 0:
#         return false
#     else:
#         return true

#we will use this in case of if-else condition:
def is_element_present(how,what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except (NoSuchElementException,ElementClickInterceptedException):
        return False

login = test_Login_page(driver)
login.enter_username("shantanu.khanna1@shipway.in")
login.enter_password("Shaan@123")
login.click_login()
driver.refresh()

for r in range(2,row+1):
    from_pincode = Pincode_data.readData(path, "Sheet1", r,1)
    to_pincode = Pincode_data.readData(path, "Sheet1",r,2)

    driver.find_element(By.XPATH,
        "//body/div[@id='main_column']/div[1]/div[1]/div[1]/div[2]/ul[1]/li[8]/a[1]").click()
    driver.find_element(By.XPATH,"//span[contains(text(),'Rate Card')]").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Rate Calculator')]").click()
    driver.find_element(By.ID,"pickup_pincode").send_keys(from_pincode)
    driver.find_element(By.ID,"drop_pincode").send_keys(to_pincode)
    driver.find_element(By.NAME,"dispatch[aggregation_rate_card.calculate_price]").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    if is_element_present(By.XPATH,
                           "/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[16]/td[7]"
                           ):
        time.sleep(4)
        print("test is passed")
        Pincode_data.writeData(path, "Sheet1", r, 3, "test passed")
    else:
        print("test failed")
        Pincode_data.writeData(path, "Sheet1", r, 3, "test failed")

driver.close()
driver.quit()
#assertEqual("",driver.find_element_by_xpath(By.XPATH,))
#driver.assertEqual("29,50",:

    # if (driver.find_element(By.XPATH, "//th[normalize-space()='Total Charges']").getText() == "Total Charges"):
    #     print("yes")
    #     Pincode_data.writeData(path, "Sheet1", r, 3, "test passed")
    # else:
    #     print("no")
    #     Pincode_data.writeData(path, "Sheet1", r, 3, "test failed")