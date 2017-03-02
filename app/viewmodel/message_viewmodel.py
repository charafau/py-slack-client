from app.model.message_model import MessageModel


class MessageViewModel(object):
    def __init__(self):
        super().__init__()
        self.model = MessageModel()

    def fetch_messages(self):
        return self.model.fetch_messages()
