from adb_controller import Device


if __name__ == "__main__":
    device = Device(
        wifi_address="10.0.0.149",
        usb_serial="18b88af1",
    )

    device.screen.wakeup_screen()
    device.screen.take_screenshot()
