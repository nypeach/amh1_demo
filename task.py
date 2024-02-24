from config import traumasoft
from top_ten import top_ten
from RPA.Browser.Selenium import Selenium
from RPA.Browser.Selenium import ChromeOptions
import time


options = ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-infobars")
options.add_argument("--test-type")
prefs = {"profile.autofill.profile_enabled": False, "autofill.profile_enabled": False}
options.add_experimental_option("prefs", prefs)
browser = Selenium(auto_close=False)



def open_traumasoft_and_login():
    login_button = 'xpath://*[@id="app"]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[2]/div/button'
    browser.open_available_browser("https://allmh.traumasoft.com/")
    browser.maximize_browser_window()
    browser.input_text("css=#input-13", traumasoft["username"])
    browser.input_text("css=#input-16", traumasoft["password"])
    browser.click_button(login_button)

def get_worklist_items():
    browser.wait_until_page_contains_element("css=#topnav_admin")
    browser.go_to("https://allmh.traumasoft.com/main.php?a=billing:workflow/main")
    browser.wait_until_page_contains_element("css=#app_view_workflowFilter")
    browser.select_from_list_by_value("css=#app_view_workflowFilter","565")
    browser.click_element("css=#app_view_startDate")
    browser.wait_until_page_contains_element("class=ui-datepicker-month")
    time.sleep(1)
    browser.click_element_when_visible("class=ui-datepicker-year")
    browser.select_from_list_by_value("class=ui-datepicker-year", "2024")
    time.sleep(1)
    browser.select_from_list_by_value("class=ui-datepicker-month", "0")
    time.sleep(1)
    browser.click_element("css=#app_view_endDate")
    browser.click_button("css=#app_view_Search")
    browser.wait_until_page_contains_element("css=#workflow_grid_Grid")
    time.sleep(1)

def get_eligibility_info():
    for row in top_ten:
        print(row)
        browser.go_to(f"https://allmh.traumasoft.com/main.php?a=billing:validation/main&popup=1#id:{row['leg_id']}")
        time.sleep(1)
        browser.click_element_when_visible("css=#app_mainView_medical")
        time.sleep(1)
        browser.click_element_when_visible("css=#app_mainView_billing")
        time.sleep(1)
        browser.click_element_when_visible("css=#app_mainView_notes")
        time.sleep(1)
        browser.click_element_when_visible("css=#app_mainView_attachments")
        time.sleep(1)
        browser.click_element_when_visible("css=#app_mainView_history")
        time.sleep(1)
        browser.press_keys("css=#otherActions", "RETURN+ARROW_UP+ARROW_UP+RETURN")
        get_payor_logic_info(row)
        edit_patient(row)
        time.sleep
        print(browser.get_window_names("CURRENT"))
        break


def get_payor_logic_info(info):
    browser.switch_window("payorLogic")
    time.sleep(2)
    browser.press_keys('xpath://*[@id="app_New"]', "RETURN")
    time.sleep(3)
    browser.click_element("css=#pl_eligibility_checkbox")
    time.sleep(1)
    browser.input_text_when_element_is_visible('xpath://*[@id="app_RunTestsDialog_EligibilityPayors_chosen"]/ul/li/input', "Medicaid - TMHP")
    browser.press_keys('xpath://*[@id="app_RunTestsDialog_EligibilityPayors_chosen"]/ul/li/input', "RETURN")
    browser.click_element('xpath:/html/body/div[5]/div[3]/div/button[1]')
    time.sleep(5)
    browser.go_to(f"https://allmh.traumasoft.com/main.php?a=billing:validation/main&popup=1#id:{info['leg_id']}")
    browser.maximize_browser_window()

def edit_patient(patient):
    browser.go_to(f"https://allmh.traumasoft.com/main.php?a=cadv3:patients/main&patient_id={patient['patient_id']}")
    browser.maximize_browser_window()
    print(browser.get_window_names("CURRENT"))



if __name__ == "__main__":
    open_traumasoft_and_login()
    get_worklist_items()
    get_eligibility_info()