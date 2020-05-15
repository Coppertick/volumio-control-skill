from mycroft import MycroftSkill, intent_file_handler


class VolumioControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.volumio.intent')
    def handle_control_volumio(self, message):
        self.speak_dialog('control.volumio')


def create_skill():
    return VolumioControl()

