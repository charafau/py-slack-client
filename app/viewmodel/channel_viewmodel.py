from app.model.channel_model import ChannelModel


class ChannelViewModel:
    def __init__(self):
        super().__init__()
        self.model = ChannelModel()

    def fetchChannels(self):
        return self.model.fetchChannels()
