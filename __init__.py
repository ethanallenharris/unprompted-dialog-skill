from mycroft import MycroftSkill, intent_handler
from datetime import datetime, timedelta
import random




MINUTES = 60 #seconds

class UnpromptedDialog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):  
        # Creates repeating event to talk unpromted  
        self.schedule_repeating_event(self.__speak, datetime.now(), 60 * MINUTES, name='unprompted')
        # If frequency list doesn't exist yet instantiate it
        if 'frequency' not in self.settings:
            self.settings['frequency'] = []
            
    def __speak(self, message):
        # Calculate the chance of speaking based on the stored frequency number
        #frequency = self.settings['frequency'][0]
        if random.randint(0, 10) <= 10:
            # Speak a random dialog
            response = self.speak_dialog(random.choice(['unprompted.generic', 'unpromted.didyouknow']))
            
    @intent_handler('change.frequency.intent')
    def handle_frequency_change(self, message):
        self.speak_dialog('unprompted.generic')



def create_skill():
    return UnpromptedDialog()
