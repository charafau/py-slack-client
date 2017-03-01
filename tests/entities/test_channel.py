from unittest import TestCase


class TestChannel(TestCase):
    def setUp(self):
        self.json = """{'id': 'C3WBCUECA', 'name': 'general', 'is_channel': True,
         'created': 1485362015, 'creator': 'U3WDY4PEH', 'is_archived': False, 'is_general': True,
          'is_member': True, 'members': ['U3WDY4PEH', 'U3X42THJB'],
          'topic': {'value': 'Company-wide announcements and work-based matters', 'creator': '', 'last_set': 0},
          'purpose': {'value': 'This channel is for team-wide communication and announcements.
          All team members are in this channel.',
          'creator': '', 'last_set': 0}, 'previous_names': [], 'num_members': 2}"""

    def test_should_be_true(self):
        self.assertTrue(True)


