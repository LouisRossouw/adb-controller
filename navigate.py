class Nav:
    def __init__(self, device):
        self.device = device

    def nav_home(self):
        self.device.adb.run("shell", "input", "keyevent", "KEYCODE_HOME")
