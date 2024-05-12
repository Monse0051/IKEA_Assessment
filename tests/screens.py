from enum import Enum

class Screens(Enum):
    WELCOME = 0
    REGION = 1
    PRIVACY = 2
    CONSENT_FOR_ANALITYCS = 3
    TERMS_AND_CONDITIONS = 4
    HOME = 5
    DIRIGERA_HUB_POP_UP = 6
    GET_STARTED = 7
    CONNECT_ETH = 8
    CONNECT_PWR = 9
    WAIT_FOR_RING = 10
    RING_LIGHT_PULSE = 11
    LOOKING_FOR_HUBS = 12

_ANDROID_WIDGET = "android.widget"
class WidgetsNames(Enum):
    TEXT_VIEW = f"{_ANDROID_WIDGET}.TextView"
    IMAGE_VIEW = f"{_ANDROID_WIDGET}.ImageView"

_ANDROID_VIEW = "android.view"
class ViewNames(Enum):
    ANDROID_VIEW = f"{_ANDROID_VIEW}.View"
