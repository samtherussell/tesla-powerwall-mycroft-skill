from mycroft import MycroftSkill, intent_file_handler
from tesla_powerwall_controller import PowerwallController

class TelsaPowerwallSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.controller = None

    def initialize(self):
      self.settings_change_callback = self.on_settings_changed
      self.on_settings_changed()

    def on_settings_changed(self):
        ip_address = self.settings.get('ip_address')
        self.log.info(f"read ip address '{ip_address}' from settings")
        if ip_address:
          self.controller = PowerwallController(ip_address)

    @intent_file_handler('battery.charge.intent')
    def battery_charge(self, message):
        if not self.controller: raise Exception('IP address of tesla powerwall not set')
        resp = self.controller.get_battery_charge()
        self.log.info(f"Response: {resp}")
        self.speak(resp)

    @intent_file_handler('power.level.intent')
    def power_level(self, message):
        if not self.controller: raise Exception('IP address of tesla powerwall not set')
        endpoint = message.data.get('endpoint')
        self.log.info(f'power.level.intent: {endpoint}')
        if endpoint == 'battery':
          resp = self.controller.get_battery_power()
        elif 'panel' in endpoint:
          resp = self.controller.get_solar_power()
        elif endpoint == 'grid':
          resp = self.controller.get_grid_power()
        elif endpoint == 'house':
          resp = self.controller.get_house_power()
        else:
          raise Exception(f'invalid endpoint: {endpoint}')
        self.log.info(f"Response: {resp}")
        self.speak(resp)

def create_skill():
    return TelsaPowerwallSkill()

