import XLUtils

from selenium import webdriver
driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.maximize_window()

path = "../POMDemo/DDTdemo.xlsx"

row = XLUtils.getRowCount(path,"sheet1")
column = XLUtils.getColumnCount(path,"sheet1")

for r in range(2,row+1):
    username = XLUtils.readData(path,"sheet1",r,1)
    password = XLUtils.readData(path,"sheet1",r,2)

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("dispatch[auth.login]").click()

    if driver.title == "Orders :: View orders - Administration panel":
        print("Test passed")
        XLUtils.writeData(path,"sheet1",r,3,"test passed")
        driver.find_element_by_xpath(
            "//body/div[@id='main_column']/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Sign out')]").click()
    else:
        print("test failed")
        XLUtils.writeData(path,"sheet1",r,3,"test failed")
        driver.refresh()

    #driver.find_element_by_xpath(
        #"//body/div[@id='main_column']/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]").click()
    #driver.find_element_by_xpath("//a[contains(text(),'Sign out')]").click()

driver.close()
driver.quit()

