# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import Optional
from ._core import Enum
from ._thread import ThreadType, ThreadColor, Thread


class TypingStatus(Enum):
    """Used to specify whether the user is typing or has stopped typing"""

    STOPPED = 0
    TYPING = 1


@attr.s(cmp=False, init=False)
class User(Thread):
    """Represents a Facebook user. Inherits `Thread`"""

    #: The profile url
    url = attr.ib(None, type=Optional[str])
    #: The users first name
    first_name = attr.ib(None, type=Optional[str])
    #: The users last name
    last_name = attr.ib(None, type=Optional[str])
    #: Whether the user and the client are friends
    is_friend = attr.ib(None, type=Optional[bool])
    #: The user's gender
    gender = attr.ib(None, type=Optional[str])
    #: From 0 to 1. How close the client is to the user
    affinity = attr.ib(None, type=Optional[float])
    #: The user's nickname
    nickname = attr.ib(None, type=Optional[str])
    #: The clients nickname, as seen by the user
    own_nickname = attr.ib(None, type=Optional[str])
    #: A :class:`ThreadColor`. The message color
    color = attr.ib(None, type=Optional[ThreadColor])
    #: The default emoji
    emoji = attr.ib(None, type=Optional[str])

    def __init__(
        self,
        uid,
        url=None,
        first_name=None,
        last_name=None,
        is_friend=None,
        gender=None,
        affinity=None,
        nickname=None,
        own_nickname=None,
        color=None,
        emoji=None,
        **kwargs
    ):
        super(User, self).__init__(ThreadType.USER, uid, **kwargs)
        self.url = url
        self.first_name = first_name
        self.last_name = last_name
        self.is_friend = is_friend
        self.gender = gender
        self.affinity = affinity
        self.nickname = nickname
        self.own_nickname = own_nickname
        self.color = color
        self.emoji = emoji


@attr.s(cmp=False)
class ActiveStatus(object):
    #: Whether the user is active now
    active = attr.ib(None, type=Optional[bool])
    #: Timestamp when the user was last active
    last_active = attr.ib(None, type=Optional[int])
    #: Whether the user is playing Messenger game now
    in_game = attr.ib(None, type=Optional[bool])
