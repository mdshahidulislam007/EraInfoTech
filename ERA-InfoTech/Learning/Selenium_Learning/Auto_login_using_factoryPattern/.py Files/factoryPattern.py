from __future__ import annotations
from abc import ABC, abstractmethod

username = 'palashdx@gmail.com'
password = 'p@101511'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Browser():

    @abstractmethod
    def myBrowser(self):
        pass


class Chrome(Browser):
    def myBrowser(self):
        driver = webdriver.Chrome(r"resources/chromedriver.exe")

        driver.set_page_load_timeout(10)
        url = 'https://www.linkedin.com/login'
        driver.get(url)

        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name('login__form_action_container ').click()

        driver.maximize_window()
        driver.refresh()
        # driver.close()


class Firefox(Browser):
    def myBrowser(self):
        driver = webdriver.Firefox(executable_path="resources/geckodriver.exe")

        driver.set_page_load_timeout(10)
        url = 'https://www.linkedin.com/login'
        driver.get(url)

        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name('login__form_action_container ').click()

        driver.maximize_window()
        driver.refresh()
        #driver.close()


ch = Chrome()
ff = Firefox()
n = input("Please Choose Browser: ")
if n == 'Chrome':
    ch.myBrowser()
elif n == 'Firefox':
    ff.myBrowser()


