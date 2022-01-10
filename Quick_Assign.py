import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True

ser = Service(executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.find_element(By.ID,"username").send_keys("shantanu.khanna1@shipway.in")
driver.find_element(By.ID,"password").send_keys("Shaan@123")
driver.find_element(By.NAME,"dispatch[auth.login]").click()
time.sleep(4)
i=1
driver.find_element(By.XPATH,"//tr[3]/td[1]/input").click()
driver.find_element(By.XPATH,"//tr[2]/td[1]/input").click()
driver.find_element(By.XPATH,"//tr[4]/td[1]/input").click()

while is_element_present(By.XPATH,"//tr["+str(i)+"]/td[1]/input"):
    driver.find_element_by_xpath("//tr["+str(i)+"]/td[1]/input").click()
    i += 1