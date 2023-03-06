from mycroft import MycroftSkill, intent_file_handler
import os

class Shutdown(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shutdown.intent')
    def handle_shutdown(self, message):
        self.speak_dialog('shutdown')
        command = "shutdown -P now"
        os.system(command)


def create_skill():
    return Shutdown()

