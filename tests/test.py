import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

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

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_ikea_app(self):
        time.sleep(0.5)
        button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
        # self.driver.page_source # XML string with the page source
        print(button)
        button.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
