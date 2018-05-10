from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class TunerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('Tuner'))
    def handle_tuner(self, message):
        self.speak_dialog('tuner')


def create_skill():
    return TunerSkill()

