# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import Set, Dict, Optional
from ._thread import ThreadType, ThreadColor, Thread


@attr.s(cmp=False, init=False)
class Group(Thread):
    """Represents a Facebook group. Inherits `Thread`"""

    #: Unique list (set) of the group thread's participant user IDs
    participants = attr.ib(
        factory=set, type=Set[str], converter=lambda x: set() if x is None else x
    )
    #: A dict, containing user nicknames mapped to their IDs
    nicknames = attr.ib(
        factory=dict, type=Dict[str, str], converter=lambda x: {} if x is None else x
    )
    #: A :class:`ThreadColor`. The groups's message color
    color = attr.ib(None, type=Optional[ThreadColor])
    #: The groups's default emoji
    emoji = attr.ib(None, type=Optional[str])
    # Set containing user IDs of thread admins
    admins = attr.ib(
        factory=set, type=Set[str], converter=lambda x: set() if x is None else x
    )
    # True if users need approval to join
    approval_mode = attr.ib(None, type=Optional[bool])
    # Set containing user IDs requesting to join
    approval_requests = attr.ib(
        factory=set, type=Set[str], converter=lambda x: set() if x is None else x
    )
    # Link for joining group
    join_link = attr.ib(None, type=Optional[str])

    def __init__(
        self,
        uid,
        participants=None,
        nicknames=None,
        color=None,
        emoji=None,
        admins=None,
        approval_mode=None,
        approval_requests=None,
        join_link=None,
        privacy_mode=None,
        **kwargs
    ):
        super(Group, self).__init__(ThreadType.GROUP, uid, **kwargs)
        if participants is None:
            participants = set()
        self.participants = participants
        if nicknames is None:
            nicknames = []
        self.nicknames = nicknames
        self.color = color
        self.emoji = emoji
        if admins is None:
            admins = set()
        self.admins = admins
        self.approval_mode = approval_mode
        if approval_requests is None:
            approval_requests = set()
        self.approval_requests = approval_requests
        self.join_link = join_link


@attr.s(cmp=False, init=False)
class Room(Group):
    """Deprecated. Use :class:`Group` instead"""

    # True is room is not discoverable
    privacy_mode = attr.ib(None, type=Optional[bool])

    def __init__(self, uid, privacy_mode=None, **kwargs):
        super(Room, self).__init__(uid, **kwargs)
        self.type = ThreadType.ROOM
        self.privacy_mode = privacy_mode
