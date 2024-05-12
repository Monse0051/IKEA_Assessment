import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from app_controller import AppController

from screens import Screens, WidgetsNames

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

class TestAppiumMainFlow:
    def setup_method(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.controller = AppController(self.driver)

    def teardown_method(self):
        self.controller.close_app()
    
    def goto_screen(self, screen: Screens):
        print(f"Navegating to screen: {screen.name}...")
        for _ in range(screen.value):
            self.controller.next_screen()


    def test_screen_welcome(self):
        """
        Test documentation
        """
        self.goto_screen(Screens.WELCOME)
        
        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  6, "Screen shall have 6 TextView elements ['welcome', 'enjoy', 'control', 'stay','easy', button_get]"

    def test_screen_region(self):
        print("region test...")
        self.goto_screen(Screens.REGION)
        
        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  3, "Screen shall have next TextView elements ['lets start', region, button_text]"

    def test_screen_privacy(self):
        print("privacy test...")
        self.goto_screen(Screens.PRIVACY)
        
        widgets_text = self.controller.find_elements("android.widget.TextView")
        print(widgets_text)
        assert len(widgets_text) ==  2, "Screen shall have next TextView elements ['privacy', 'tack for...']"
        button = self.controller.find_button("primary")
        assert not button.is_enabled()

    def test_screen_consent(self):
        print("consent test...")
        self.goto_screen(Screens.CONSENT_FOR_ANALITYCS)

        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  6, "Screen shall have next TextView elements ['consent', 'vi IKEA...', 'Ja Jag...', ]"        
        check_box_consent = self.controller.find_element_by_id("consent_checkbox")
        check_box_no_consent = self.controller.find_element_by_id("no_consent_checkbox")
        assert not check_box_consent.is_selected()
        assert not check_box_no_consent.is_selected()

    def test_screen_terms_and_conditions(self):
        print("consent test...")
        self.goto_screen(Screens.TERMS_AND_CONDITIONS)
        
        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  3, "Screen shall have next TextView elements ['terms and conditions', 'please read...', 'vilkor for...']"
        button = self.controller.find_button("primary")
        assert not button.is_enabled()
    
    def test_screen_home(self):
        print("home test..")
        self.goto_screen(Screens.HOME)

        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  5, "Screen shall have next TextView elements []"
        button = self.controller.find_element_by_class_name("android.widget.Button")
        assert button.is_enabled()

    def test_screen_dirigera_hub_pop_up(self):
        print("dirigera hub pop up..")
        self.goto_screen(Screens.DIRIGERA_HUB_POP_UP)

        widgets_text = self.controller.find_elements("android.widget.TextView")
        assert len(widgets_text) ==  3, "Screen shall have next TextView elements ['why use', 'the hub is...', 'Add a DIRIGERA hub']"

    def test_screen_get_started(self):
        print("get started..")
        self.goto_screen(Screens.GET_STARTED)

        widgets_text = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(widgets_text) == 7, "Screen shall have next TextView elements ['']"
        widgets_images = self.controller.find_elements(WidgetsNames.IMAGE_VIEW.value)
        assert len(widgets_images) == 4
        assert widgets_images[0].get_attribute("content-desc") == "Hub"
        assert widgets_images[1].get_attribute("content-desc") == "Cables and plug"
        assert widgets_images[2].get_attribute("content-desc") == "Power"
        assert widgets_images[3].get_attribute("content-desc") == "Router"

    def test_screen_connect_eth(self):
        self.goto_screen(Screens.CONNECT_ETH)
        images = self.controller.find_elements(WidgetsNames.IMAGE_VIEW.value)
        assert len(images) == 1
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 3
        content_descs = [w.get_attribute("text")  for w in texts_widgets]

        assert content_descs == ['Connect the ethernet cable to the hub and your router',
                                 'The router will connect the hub to your home internet network.',
                                 'Next']
        
    def test_screen_connect_pwr(self):
        self.goto_screen(Screens.CONNECT_PWR)
        images = self.controller.find_elements(WidgetsNames.IMAGE_VIEW.value)
        assert len(images) == 1
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 3
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        #TODO check expected values ...
        print(content_descs)

    def test_screen_wait_for_ring(self):
        self.goto_screen(Screens.WAIT_FOR_RING)
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 6
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        print(content_descs)
        expected_text_contents = [
            'Wait for the ring light to make a full circle',
            'It may take a few minutes for the ring light to completely fill.',
            'Are you joining someone’s hub?',
            'If the hub is already set up, you will see a solid centre light instead of the ring.',
            'I need help',
            'Next'
            ]
        assert content_descs == expected_text_contents

    def test_screen_ring_pulse(self):
        self.goto_screen(Screens.RING_LIGHT_PULSE)
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 4
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        print(content_descs)
        expected_text_contents = [
            'The ring light will pulse when the hub is ready',
            'You will see a solid centre light instead of a ring if the hub was already up and running.',
            'I need help',
            'Next'
        ]
        assert content_descs == expected_text_contents
        

    def test_screen_looking_hubs(self):
        self.goto_screen(Screens.LOOKING_FOR_HUBS)
        time.sleep(1)
