# Android ADB Controller

- WIP

To automate a physical Android device.

### Requirements:

1. Download and install Android Debug Bridge (ADB): https://developer.android.com/tools/adb
2. Add the ADB installation directory to your system's PATH environment variable.

### Connect via USB:

1. Enable Developer Options on your Android device.
2. Enable USB Debugging.
3. Connect your device to your computer using a USB cable.

4. In a terminal, run:
   adb devices

5. Authorise the computer on your phone if prompted.

6. Copy the device serial from the output, for example:
   List of devices attached
   18b88af1 device

7. Create a device using the USB serial:
   device = Device(usb_serial="18b88af1")

### Connect via Wi-Fi

Your device must first be connected over USB.

1. Find your phone's IP address (e.g. 10.0.0.149).

2. Create the device using both the USB serial and Wi-Fi address:
   device = Device(
   usb_serial="18b88af1",
   wifi_address="10.0.0.149"
   )

3. Enable wireless ADB:
   device.adb.connect_wifi_device()
4. Once connected, you can disconnect the USB cable and continue communicating with the device over Wi-Fi.
