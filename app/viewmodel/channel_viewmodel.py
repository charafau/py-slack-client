from app.model.channel_model import ChannelModel


class ChannelViewModel:
    def __init__(self):
        super().__init__()
        self.model = ChannelModel()

    def fetch_channels(self):
        return self.model.fetch_channels()
