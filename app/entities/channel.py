from typing import NamedTuple


class Channel(NamedTuple):
    id: str
    name: str
    is_channel: bool
    created: complex
    creator: str
    is_archived: bool
    is_general: bool
    is_member: bool
    members: list
    topic: str
    purpose: str
    previous_names: list
    num_members: int
