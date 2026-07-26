

class Power:
    def __init__(self, device):
        self.device = device

    def is_state_on(self):
        return "state=ON" in self.device.get_power_stats()

    def set_state_on(self):
        self.device.screen.wakeup_screen()
