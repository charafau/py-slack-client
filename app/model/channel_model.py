import rx
from rx import Observable, Observer
from slackclient import SlackClient
from app.entities.channel import Channel
import colander
import os


class ChannelModel:
    def __init__(self):
        super().__init__()

    def fetchChannels(self):
        schema = Channel()
        return self.rx_request('channels.list').map(lambda val: val['channels'])
        # need to add this transform here later
        # .map(lambda value, index: (schema.deserialize(value)))

    def rx_request(self, method, **kwargs):
        def subscribe(observer):
            #TODO: need to create singleton of this SlackClient and inject it here somehow...
            token = os.environ['SLACK_API_TOKEN']
            sc = SlackClient(token)
            result = sc.api_call(method, **kwargs)
            observer.on_next(result)
            observer.on_completed()

        return rx.Observable.create(subscribe)
