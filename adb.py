import subprocess
import time


class ADB:
    def __init__(self, device):
        self.device = device

    def connect_wifi_device(self, port=5555):
        if not self.device.usb_serial:
            raise RuntimeError("USB serial is required.")

        if not self.device.wifi_address:
            raise RuntimeError("Wi-Fi address is required.")

        subprocess.run([
            "adb",
            "-s",
            self.device.usb_serial,
            "tcpip",
            str(port),
        ], check=True)

        time.sleep(2)

        subprocess.run([
            "adb",
            "connect",
            f"{self.device.wifi_address}:{port}",
        ], check=True)

    def run(self, *args):
        cmd = ["adb", "-s", self.device.device_id] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)

        return result.stdout.strip()

    def run_binary(self, *args):
        cmd = ["adb", "-s", self.device.device_id] + list(args)

        result = subprocess.run(
            cmd,
            capture_output=True,
            check=True,
        )

        return result.stdout
