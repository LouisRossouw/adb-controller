

if __name__ == "__main__":
    from device import Device

    device = Device(wifi_address="10.0.0.149", usb_serial="18b88af1")

    # device.adb.connect_wifi_device()

    device.screen.wakeup_screen()
    device.screen.take_screenshot()

    # res = device.instagram.is_app_focused()
    # print(res)

    # phone.wakeup_screen()
    # phone.swipe(500, 2000, 500, 1000)

    # phone.tap(550, 1447)

    # phone.open_app("com.instagram.android")

    # phone.test("kpow_636")

    # time.sleep(5)
    # phone.test("time.in.progress")

    # time.sleep(5)

    # phone.test("minecraft")
