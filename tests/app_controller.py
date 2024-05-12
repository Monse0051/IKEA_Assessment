import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from xpaths import xpaths_map
#xml_welcome = self.driver.page_source # XML string with the page source
class AppController:
    def __init__(self, driver: webdriver.webdriver.WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(15)
        self.current = 0
        # each element should be the necessary action to go to next screen
        self._transition_actions = [
            [ self.click_button ], # transition to region screen
            [ lambda : self.click_button("primary") ], # transition to privacy screen
            [   
                lambda : self._scrolling_down_until("primary"), # transition to consent for analitics screen
                lambda : self.click_button("primary")
            ],
            [   
                lambda : self.check_checkbox("consent_checkbox"), # transition to terms and conditions screen
                lambda : self.click_button("primary")
            ],
            [   
                lambda : self._scrolling_down_until("primary"), # transition to home screen
                lambda : self.click_button("primary")
            ],
            
            [ self.click_button ], # transition to dirigera hub pop up screen

            [
               lambda : self.click_button_xpath(xpaths_map["button_dirigera_hub"]), #transition to get started screen
            ],
            [ lambda: self.click_button_xpath(xpaths_map["button_get_started"])], #transition to connect eth screen

            [ lambda: self.click_button_xpath(xpaths_map["button_eth_next"])], #transition to connect pwr screen

            [ lambda: self.click_button_xpath(xpaths_map["button_connect_power_next"])], #transition to wait for ring screen

            [ lambda: self.click_button_xpath(xpaths_map["button_wait_for_ring_next"])], #transition to ring light screen

            [ lambda: self.click_button_xpath(xpaths_map["button_ring_pulse_next"])], #transition to Looking hubs screen(last one)

            
        ]

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
    
    def find_element(self, xpath:str):
        return self._driver.find_element(AppiumBy.XPATH, xpath)
    
    def find_element_by_id(self, id):
        return self._driver.find_element(AppiumBy.ID, id)
    
    def find_element_by_class_name(self, class_name):
        return self._driver.find_element(AppiumBy.CLASS_NAME, class_name)
    
    def find_elements(self, class_name):
        return self._driver.find_elements(AppiumBy.CLASS_NAME, class_name)

    def scroll_down(self):
        win_size = self._driver.get_window_size()
        x = win_size["width"]//2
        y = win_size["height"]//2
        self._driver.swipe(x, y, x, y-400, 30)

    def _scrolling_down_until(self, button_id):
        button = self.find_button(button_id)
        while not button.is_enabled():
            self.scroll_down()
    
    def check_checkbox(self, id):
        checkbox = self._driver.find_element(AppiumBy.ID, id)
        checkbox.click()

    def click_button_xpath(self, xpath):
        button = self.find_element(xpath)
        button.click()


    def close_app(self):
        if self._driver:
            self._driver.quit()

    def next_screen(self):
        actions = self._transition_actions[self.current]
        print(f"current screen {self.current}")
        for action in actions:
            action()
            # delay to give enough time to transition
            time.sleep(0.2)

        self.current += 1
    

            