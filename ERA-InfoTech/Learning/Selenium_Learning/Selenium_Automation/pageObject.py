from page_objects import PageObject, PageElement
from selenium import webdriver

class LoginPage(PageObject):
        username = PageElement(id_='username')
        password = PageElement(id_='password')
        login = PageElement(class_name='login__form_action_container ')

driver = webdriver.Chrome(r"resources/chromedriver.exe")
driver.get("https://www.linkedin.com/login")
page = LoginPage(driver)
page.username = 'palashdx@gmail.com'
page.password = 'p@101511'
page.login.click()


"""        
id_ =	Element ID attribute
css  =	CSS Selector
name  =	Element name attribute
class_name =	Element class name
tag_name  =	Element HTML tag name
link_text  =	Anchor Element text content
partial_link_text =	Anchor Element partial text content
xpath =	XPath
"""