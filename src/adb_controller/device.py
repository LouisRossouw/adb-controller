from .adb import ADB
from .app import App
from .input import Input
from .power import Power
from .navigate import Nav
from .screen import Screen
from .package.instagram import Instagram


class Device:

    def __init__(self, wifi_address=None, usb_serial=None):

        self.wifi_address = wifi_address
        self.usb_serial = usb_serial

        if wifi_address:
            self.connection_type = "wifi"
        elif usb_serial:
            self.connection_type = "usb"
        else:
            self.connection_type = None

        self.adb = ADB(self)

        self.power = Power(self)
        self.screen = Screen(self)
        self.input = Input(self)
        self.app = App(self)
        self.nav = Nav(self)

        self.instagram = Instagram(self)

    @property
    def device_id(self):
        if self.connection_type == "wifi":
            return self.wifi_address
        return self.usb_serial

    def get_power_stats(self):
        return self.adb.run("shell", "dumpsys", "power")

    def get_window_stats(self):
        return self.adb.run("shell", "dumpsys", "window")

    def get_focused(self):
        for line in self.get_window_stats().splitlines():
            if "mCurrentFocus" in line:
                return line
