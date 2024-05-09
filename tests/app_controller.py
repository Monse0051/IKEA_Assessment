import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

#xml_welcome = self.driver.page_source # XML string with the page source
class AppController:
    def __init__(self, driver: webdriver.webdriver.WebDriver):
        self._driver = driver
        time.sleep(0.1)

    def click_button(self, id = ""):
        time.sleep(0.2)
        if id != "":
            button = self._driver.find_element(AppiumBy.ID, id)
        else:   
            button = self._driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
        
        button.click()
        time.sleep(0.1)

    def get_page_source(self):
        return self._driver.page_source
    
    def find_button(self, id):
        return self._driver.find_element(AppiumBy.ID, id)
    
    def find_element(self, xpath):
        return self._driver.find_element(AppiumBy.XPATH, xpath)

    def scroll_down(self):
        win_size = self._driver.get_window_size()
        x = win_size["width"]//2
        y = win_size["height"]//2
        self._driver.swipe(x, y, x, y-200, 30)
    
    def check_checkbox(self, id):
        checkbox = self._driver.find_element(AppiumBy.ID, id)
        checkbox.click()
        time.sleep(0.1)

    