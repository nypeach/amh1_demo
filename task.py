from config import traumasoft
from RPA.Browser.Selenium import Selenium
from RPA.Browser.Selenium import WebDriverCreator
from RPA.Browser.Selenium import selenium_webdriver
import time


browser = Selenium(auto_close=False)

# Element Locators
login_button = 'xpath://*[@id="app"]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[2]/div/button'

def open_traumasoft_and_login():
    browser.open_available_browser("https://allmh.traumasoft.com/")
    # browser.maximize_browser_window()
    browser.input_text("css=#input-13", traumasoft["username"])
    browser.input_text("css=#input-16", traumasoft["password"])
    browser.click_button(login_button)

def get_worklist_items():
    # browser.wait_until_element_is_visible("css=topnav_top ")
    # time.sleep(1)
    browser.wait_until_page_contains_element("css=#topnav_admin")
    # browser.click_element('//*[@id="topnav_admin"]/ul[1]/li[2]/ul/li[20]/a')
    browser.go_to("https://allmh.traumasoft.com/main.php?a=billing:workflow/main")



if __name__ == "__main__":
    open_traumasoft_and_login()
    get_worklist_items()