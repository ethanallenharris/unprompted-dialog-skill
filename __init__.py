from mycroft import MycroftSkill, intent_handler


class UnpromptedDialog(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('dialog.unprompted.intent')
    def handle_dialog_unprompted(self, message):
        self.speak_dialog('dialog.unprompted')


def create_skill():
    return UnpromptedDialog()

