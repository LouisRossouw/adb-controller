

class Input:
    def __init__(self, device):
        self.device = device

    def tap(self, x, y):
        self.device.adb.run("shell", "input", "tap", str(x), str(y))

    def swipe(self, x_start, y_start, x_end, y_end):
        self.device.adb.run("shell", "input", "swipe", str(x_start),
                            str(y_start), str(x_end), str(y_end))

    def text(self, text):
        text = text.replace(" ", "%s")

        self.device.adb.run(
            "shell",
            "input",
            "text",
            text,
        )
