class App:

    def __init__(self, device):
        self.device = device

    def open(self, package):
        self.device.adb.run(
            "shell",
            "monkey",
            "-p",
            package,
            "1"
        )

    def is_app_focused(self, app):
        return app in self._get_focused()

    def stop(self, package):
        self.device.adb.run(
            "shell",
            "am",
            "force-stop",
            package,
        )
