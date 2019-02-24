# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import Optional
from ._attachment import Attachment


@attr.s(cmp=False)
class LocationAttachment(Attachment):
    """Represents a user location

    Latitude and longitude OR address is provided by Facebook
    """

    #: Latitude of the location
    latitude = attr.ib(None, type=Optional[float])
    #: Longitude of the location
    longitude = attr.ib(None, type=Optional[float])
    #: URL of image showing the map of the location
    image_url = attr.ib(None, type=Optional[str], init=False)
    #: Width of the image
    image_width = attr.ib(None, type=Optional[int], init=False)
    #: Height of the image
    image_height = attr.ib(None, type=Optional[int], init=False)
    #: URL to Bing maps with the location
    url = attr.ib(None, type=Optional[str], init=False)
    # Address of the location
    address = attr.ib(None, type=Optional[str])

    # Put here for backwards compatibility, so that the init argument order is preserved
    uid = attr.ib(None, type=Optional[str])


@attr.s(cmp=False, init=False)
class LiveLocationAttachment(LocationAttachment):
    """Represents a live user location"""

    #: Name of the location
    name = attr.ib(None, type=Optional[str])
    #: Timestamp when live location expires
    expiration_time = attr.ib(None, type=Optional[int])
    #: True if live location is expired
    is_expired = attr.ib(None, type=Optional[bool])

    def __init__(self, name=None, expiration_time=None, is_expired=None, **kwargs):
        super(LiveLocationAttachment, self).__init__(**kwargs)
        self.expiration_time = expiration_time
        self.is_expired = is_expired
