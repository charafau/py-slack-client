import rx
from rx import Observable, Observer
from slackclient import SlackClient
from app.entities.channel import Channel
import colander
import os


class ChannelModel(object):
    def __init__(self):
        super().__init__()

    def fetchChannels(self) -> Observable:
        return self.rx_request('channels.list').map(lambda val: val['channels']) \
            .map(lambda dictionaries: [Channel(**dictionary) for dictionary in dictionaries])

    def rx_request(self, method, **kwargs) -> Observable:
        def subscribe(observer):
            token = os.environ['SLACK_API_TOKEN']
            sc = SlackClient(token)
            result = sc.api_call(method, **kwargs)
            observer.on_next(result)
            observer.on_completed()

        return rx.Observable.create(subscribe)
