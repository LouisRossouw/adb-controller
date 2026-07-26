

class Instagram:

    URL = "https://www.instagram.com"
    PACKAGE = "com.instagram.android"

    def __init__(self, device):
        self.device = device

    def open(self):
        self.device.app.open(self.PACKAGE)

    def post_reel(self):
        ...

    def is_app_focused(self):
        return self.PACKAGE in self.device.get_focused()

    def open_account(self, acc):
        self.device.adb.run("shell", "am", "start", "-a", "android.intent.action.VIEW",
                            "-d", f"{self.URL}/{acc}/")

    def close(self):
        self.device.app.stop(self.PACKAGE)
