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
            LOGGER.info(note)
            title = note + ".mp3" 
            self.process = play_mp3(join(dirname(__file__), "mp3s", title))
            time.sleep(3)

    @intent_handler(IntentBuilder("TuningsIntent").require('Tuner'))
    def handle_play_tuning(self, message):
        utter = message.data['utterance']
        tuning_names = ['standard', 'dadgad']
        tuning_notes = {
                'standard': ['E', 'A', 'D', 'G', 'B', 'E_high'],
                'dadgad': ['D', 'A', 'D', 'G', 'A', 'D']
        }

        for tuning in tuning_names:
            if tuning in utter:
               self.play_tuning(tuning, tuning_notes[tuning]) 

def create_skill():
    return TunerSkill()

