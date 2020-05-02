from mycroft import MycroftSkill, intent_file_handler


class TelsaPowerwallUtility(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('utility.powerwall.telsa.intent')
    def handle_utility_powerwall_telsa(self, message):
        self.speak_dialog('utility.powerwall.telsa')


def create_skill():
    return TelsaPowerwallUtility()

