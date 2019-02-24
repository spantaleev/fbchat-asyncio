# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import List, Optional


@attr.s(cmp=False)
class Poll(object):
    """Represents a poll"""

    #: ID of the poll
    uid = attr.ib(None, type=Optional[str], init=False)
    #: Title of the poll
    title = attr.ib(type=str)
    #: List of :class:`PollOption`, can be fetched with :func:`fbchat.Client.fetchPollOptions`
    options = attr.ib(type=List["PollOption"])
    #: Options count
    options_count = attr.ib(None, type=Optional[int], init=False)


@attr.s(cmp=False)
class PollOption(object):
    """Represents a poll option"""

    #: ID of the poll option
    uid = attr.ib(None, type=Optional[str], init=False)
    #: Text of the poll option
    text = attr.ib(type=str)
    #: Whether vote when creating or client voted
    vote = attr.ib(False, type=bool)
    #: ID of the users who voted for this poll option
    voters = attr.ib(None, type=Optional[List[str]], init=False)
    #: Votes count
    votes_count = attr.ib(None, type=Optional[int], init=False)
