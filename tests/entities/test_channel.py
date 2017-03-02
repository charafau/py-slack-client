from unittest import TestCase

from app.entities.channel import Channel


class TestChannel(TestCase):
    def setUp(self):
        self.channel_dict = {'id': 'C3WBCUECA', 'name': 'general', 'is_channel': True, 'created': 1485362015,
                             'creator': 'U3WDY4PEH', 'is_archived': False, 'is_general': True, 'is_member': True,
                             'members': ['U3WDY4PEH', 'U3X42THJB'],
                             'topic': {'value': 'Company-wide announcements and work-based matters',
                                       'creator': '', 'last_set': 0},
                             'purpose': {
                                 'value': 'This channel is for team-wide communication and '
                                          'announcements.All team members are in this channel.',
                                 'creator': '', 'last_set': 0}, 'previous_names': [], 'num_members': 2}

    def test_should_create_object_from_dict(self):
        channel = Channel(**self.channel_dict)
        self.assertEquals(channel.id, 'C3WBCUECA')
        self.assertEquals(channel.name, 'general')
        self.assertEquals(channel.created, 1485362015)
        self.assertEquals(channel.is_channel, True)
