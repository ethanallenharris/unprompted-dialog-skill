from mycroft import MycroftSkill, intent_handler
import random




MINUTES = 1 #seconds

class UnpromptedDialog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.listen_event = None
        
    def initialize(self):  
        # Creates repeating event to talk unpromted  
        self.schedule_repeating_event(self.speak, datetime.now(), 60 * MINUTES, name='unprompted')
        # If frequency list doesn't exist yet instantiate it
        if 'frequency' not in self.settings:
            self.settings['frequency'] = [10]
            
    def speak(self):
        # Calculate the chance of speaking based on the stored frequency number
        frequency = self.settings['frequency'][0]
        if random.randint(0, 10) <= frequency:
            # Speak a random dialog
            self.speak_dialog(random.choice(['unprompted.generic', 'unpromted.didyouknow']))
            # Listen for a response
            response = self.get_response('prompt')
