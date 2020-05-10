import unittest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory

class LoginPage(PageFactory):

    def __init__(self, driver):
               self.driver = driver

    locators = {
        "edtUserName": ('ID', 'username'),
        "edtPassword": ('ID', 'password'),
        "btnSignIn": ('XPATH', "//button[@class='btn__primary--large from__button--floating']")
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("palashdx@gmail.com")  # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("p@101511")
        self.btnSignIn.click_button()

class LoginTest():

    def test_Login(self):
        driver = webdriver.Chrome(r"resources/chromedriver.exe")
        driver.get("https://www.linkedin.com/login")

        pglogin = LoginPage(driver)
        pglogin.login()

t = LoginTest()
t.test_Login()
