from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"resources/chromedriver.exe")
url = 'http://10.11.201.92:4200/fileProcessing/'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//div[@id='cdk-step-content-0-0']//div[1]//div[1]//div[1]//div[2]//button[1]//span[1]//mat-icon[1]").click()
driver.find_element_by_tag_name("input").send_keys("C:/Users/shahidul/PycharmProjects/f.xls")
driver.find_element_by_xpath("//button[@class='btn btn-info mat-raised-button']").click()