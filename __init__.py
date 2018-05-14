from os.path import dirname, join
import time
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util import play_mp3
from mycroft.util.log import getLogger
from mycroft.audio import wait_while_speaking

LOGGER = getLogger(__name__)

class TunerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def play_tuning(self, tuning, notes):
        self.load_data_files(dirname(__file__))
        self.speak("Playing the notes for " + tuning)
        wait_while_speaking()
        for note in notes:
            title = note + "_" + self.settings["play_duration"] + ".mp3" 
            self.process = play_mp3(join(dirname(__file__), 
                self.settings["instrument_select"], title))
            time.sleep(3)

    @intent_handler(IntentBuilder("TuningsIntent").require('Tuner'))
    def handle_play_tuning(self, message):
        utter = message.data['utterance']
        tuning_names = ['standard', 'drop d', 'half step down']
        tuning_notes = {
                'standard': ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
                'drop d': ['D2', 'A2', 'D3', 'G3', 'B3', 'E4'],
                'half step down': ['Ds2', 'Gs2', 'Cs3', 'Fs3', 'As3', 'Ds4']
        }

        for tuning in tuning_names:
            if tuning in utter:
                self.play_tuning(tuning, tuning_notes[tuning]) 
                return True

        self.speak("That is an unsupported tuning.")


def create_skill():
    return TunerSkill()

