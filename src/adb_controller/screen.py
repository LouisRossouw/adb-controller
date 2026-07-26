from pathlib import Path


class Screen:
    def __init__(self, device):
        self.device = device

    def wakeup_screen(self):
        self.device.adb.run("shell", "input", "keyevent", "KEYCODE_WAKEUP")

    def get_screen_size(self):
        self.device.adb.run("shell", "wm", "size")

    def take_screenshot(self, filename="screen.png"):
        data = self.device.adb.run_binary(
            "exec-out",
            "screencap",
            "-p",
        )

        path = Path(filename)
        path.write_bytes(data)

        return path

    def is_locked(self):
        return "isStatusBarKeyguard=true" in self.device.get_window_stats()

    def unlock(self):
        ...
