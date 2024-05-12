import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from app_controller import AppController

from screens import Screens, WidgetsNames, ViewNames

from xpaths import xpaths_map

capabilities = dict(
    platformName='Android',
    platformVersion='14',
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
        self.goto_screen(Screens.WELCOME)
        
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 6
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        assert content_descs == ['Hej! Welcome to the\nIKEA Home smart app', 
                                 'Enjoy a smarter life at home that leaves you free for the things you love most.', 
                                 'Control your home from anywhere', 'Stay connected with notifications', 
                                 'Easy to use for the whole family', 'Get started']


    def test_screen_region(self):
        print("region test...")
        self.goto_screen(Screens.REGION)

        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 3
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        assert content_descs == ["Let's start with your region", 
                                 'We’ll provide local Terms & Conditions so you know what to expect from the app.', 
                                 'Sweden']
        button_regions = self.controller.find_element(xpaths_map["button_regions"])
        assert button_regions.is_enabled

    def test_screen_privacy(self):
        print("privacy test...")
        self.goto_screen(Screens.PRIVACY)
        
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) ==  2, "Screen shall have next TextView elements ['privacy', 'tack for...']"
        button = self.controller.find_button("primary")
        assert not button.is_enabled()

    def test_screen_consent(self):
        print("consent test...")
        self.goto_screen(Screens.CONSENT_FOR_ANALITYCS)

        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) ==  6 #TODO: create a json to have the text there.        
        check_box_consent = self.controller.find_element_by_id("consent_checkbox")
        check_box_no_consent = self.controller.find_element_by_id("no_consent_checkbox")
        assert not check_box_consent.is_selected()
        assert not check_box_no_consent.is_selected()

    def test_screen_terms_and_conditions(self):
        print("terms and conditions test...")
        self.goto_screen(Screens.TERMS_AND_CONDITIONS)
        
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) ==  3
        button = self.controller.find_button("primary")
        assert not button.is_enabled()
    
    def test_screen_home(self):
        print("home test..")
        self.goto_screen(Screens.HOME)

        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) ==  5
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        assert content_descs == ['Home screen', 
                                 'Create rooms and add products', 
                                 'Control everything with one tap', 
                                 'Add DIRIGERA hub and let’s go!', 'Add a DIRIGERA hub']
        button = self.controller.find_element_by_class_name("android.widget.Button")
        assert button.is_enabled()

        view_widgets = self.controller.find_elements(ViewNames.ANDROID_VIEW.value)
        content_descs_views = [w.get_attribute("content-desc")  for w in view_widgets if w.get_attribute("content-desc")!="null" and w.get_attribute("content-desc")!=""]
        assert content_descs_views == ['Home screen', 'All scenes list', 'Energy Insights', 'User profile and settings']

    def test_screen_dirigera_hub_pop_up(self):
        print("dirigera hub pop up test..")
        self.goto_screen(Screens.DIRIGERA_HUB_POP_UP)

        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) ==  3
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        assert content_descs == ['Why use a DIRIGERA hub?', 
                                 'The hub is the heart of the smart home and keeps everything in harmony.\n\nRemote access, notifications, scenes and more; the hub provides a whole host of extras to make life at home a little bit smarter.', 
                                 'Add a DIRIGERA hub']

    def test_screen_get_started(self):
        print("get started test..")
        self.goto_screen(Screens.GET_STARTED)

        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 7
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        assert content_descs == ["Let's get started!", 
                                 "Here are the parts you'll need:", 
                                 'Hub', 'Cables and plug', 'Power', 'Router', 'Get started']
        
        widgets_images = self.controller.find_elements(WidgetsNames.IMAGE_VIEW.value)
        assert len(widgets_images) == 4
        assert widgets_images[0].get_attribute("content-desc") == "Hub"
        assert widgets_images[1].get_attribute("content-desc") == "Cables and plug"
        assert widgets_images[2].get_attribute("content-desc") == "Power"
        assert widgets_images[3].get_attribute("content-desc") == "Router"

    def test_screen_connect_eth(self):
        print("connect eth test..")
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
        print("connect pwr test..")
        self.goto_screen(Screens.CONNECT_PWR)
        images = self.controller.find_elements(WidgetsNames.IMAGE_VIEW.value)
        assert len(images) == 1
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 3
        content_descs = [w.get_attribute("text")  for w in texts_widgets]

        assert content_descs == ['Connect the power cable to the hub and plug it in', 
                                 'The hub will start up as soon as the ethernet cable and power cable are connected.', 
                                 'Next']

    def test_screen_wait_for_ring(self):
        print("wait for ring test..")
        self.goto_screen(Screens.WAIT_FOR_RING)
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 6
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        expected_text_contents = [
            'Wait for the ring light to make a full circle',
            'It may take a few minutes for the ring light to completely fill.',
            'Are you joining someone’s hub?',
            'If the hub is already set up, you will see a solid centre light instead of the ring.',
            'I need help',
            'Next'
            ]
        assert content_descs == expected_text_contents
        help_button = self.controller.find_element(xpaths_map["button_need_help"])
        assert help_button.is_enabled

    def test_screen_ring_pulse(self):
        print("ring pulse test..")
        self.goto_screen(Screens.RING_LIGHT_PULSE)
        texts_widgets = self.controller.find_elements(WidgetsNames.TEXT_VIEW.value)
        assert len(texts_widgets) == 4
        content_descs = [w.get_attribute("text")  for w in texts_widgets]
        expected_text_contents = [
            'The ring light will pulse when the hub is ready',
            'You will see a solid centre light instead of a ring if the hub was already up and running.',
            'I need help',
            'Next'
        ]
        assert content_descs == expected_text_contents
        help_button = self.controller.find_element(xpaths_map["button_need_help"])
        assert help_button.is_enabled
        

    def test_screen_looking_hubs(self):
        print("looking hubs test..")
        self.goto_screen(Screens.LOOKING_FOR_HUBS)
        text_widget = self.controller.find_element_by_class_name("android.widget.TextView")
        content_descs = text_widget.get_attribute("text")
        assert content_descs == "Looking for nearby hubs..."
        time.sleep(1)
