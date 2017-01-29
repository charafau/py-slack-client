import rx

from app.model import slack_client


class ChannelModel:
    def __init__(self):
        super().__init__()

    def fetch_channels(self):
        return self.rx_request('channels.list').map(lambda val: val['channels'])
        # need to add this transform here later
        # .map(lambda value, index: (schema.deserialize(value)))

    @staticmethod
    def rx_request(method, **kwargs):
        def subscribe(observer):
            # TODO: need to create singleton of this SlackClient and inject it
            # here somehow...
            result = slack_client.api_call(method, **kwargs)
            observer.on_next(result)
            observer.on_completed()

        return rx.Observable.create(subscribe)
