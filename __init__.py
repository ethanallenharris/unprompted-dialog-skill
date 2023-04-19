from mycroft import MycroftSkill, intent_handler
from datetime import *
import random


MINUTES = 60 #seconds

FREQUENCY = 60 #minutes


class UnpromptedDialog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self): 
        self.settings['dialogOptions'] = ['unprompted.generic', 'unpromted.didyouknow', 'unpromted.affirmation', 'unprompted.relationship', 'unprompted.selfimprovement', 'unprompted.spiritual']
        # Creates repeating event to talk unpromted  
        self.schedule_repeating_event(self.__speak, datetime.now(), FREQUENCY * MINUTES, name='unprompted')
        # If frequency list doesn't exist yet instantiate it
        if 'frequency' not in self.settings:
            self.settings['frequency'] = 10
            
    def __speak(self, message):
        current_time = datetime.now().time()
        # If the current time is before 11 am or after 8 pm, do not activate/talk
        if current_time < time(11) or current_time > time(20):
            return  # Return and exit the function
        
        
        # Calculate the chance of speaking based on the stored frequency number
        if random.randint(1, 10) <= self.settings['frequency']:
            # Speak a random dialog
            response = self.speak_dialog(random.choice(self.settings['dialogOptions']))
            
    @intent_handler('change.frequency.intent')
    def handle_frequency_change(self, message):
        # Get user desired change for frequency
        frequency_change = message.data.get('frequency')
        
        if 'more' in frequency_change:
            # Checks frequency variable is in range
            if self.settings['frequency'] != 10:
                self.settings['frequency'] += 1
                self.speak_dialog('frequency.change', data={"frequency":"more"})
                
        elif 'less' in frequency_change:
            # Checks frequency variable is in range
            if self.settings['frequency'] != 0:
                self.settings['frequency'] -= 1
                self.speak_dialog('frequency.change', data={"frequency":"less"})
                
    
    
    @intent_handler('stop.intent')
    def handle_frequency_stop(self, message):
        # If user asks mycroft to stop talking unprompted, set to 0
        self.settings['frequency'] = 0
        # Says ' Okay I will no longer take the initiative to talk'
        self.speak_dialog('stop')
        
        
    #update frequency from webapp intent
    @intent_handler('update.intent')
    def handle_update(self, message):
        FREQUENCY = int(message.data.get('time'))
        
    
    
            
        

def create_skill():
    return UnpromptedDialog()
