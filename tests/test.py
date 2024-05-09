import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from app_controller import AppController

from xpaths import xpaths_map

capabilities = dict(
    platformName='Android',
    platformVersion='13',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage = 'com.ikea.inter.homesmart.system2',
    appActivity= 'com.ikea.system2.start.StartActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.controller = AppController(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
    
    def _scrolling_down(self, button_id):
        button = self.controller.find_button(button_id)
        while not button.is_enabled():
            self.controller.scroll_down()


    def test_ikea_app_main_flow(self):
        
        self.controller.click_button()

        self.controller.click_button("primary")

        self._scrolling_down("primary")
        
        self.controller.click_button("primary")

        self.controller.check_checkbox("consent_checkbox")

        self.controller.click_button("primary")

        self._scrolling_down("primary")

        #go to home screen
        self.controller.click_button("primary")

        #Add hub from home page
        self.controller.click_button()

        button = self.controller.find_element(xpaths_map["button_dirigera_hub"])
        button.click()

        button = self.controller.find_element(xpaths_map["button_get_started"])
        button.click()

        button = self.controller.find_element(xpaths_map["button_eth_next"])
        button.click()

        button = self.controller.find_element(xpaths_map["button_connect_power_next"])
        button.click()

        button = self.controller.find_element(xpaths_map["button_wait_for_ring_next"])
        button.click()

        button = self.controller.find_element(xpaths_map["button_ring_pulse_next"])
        button.click()
        time.sleep(5)

        # source_page = self.driver.page_source
        # print(source_page)
        
        


if __name__ == '__main__':
    unittest.main()
