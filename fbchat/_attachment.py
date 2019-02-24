# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import List, Optional


@attr.s(cmp=False)
class Attachment(object):
    """Represents a Facebook attachment"""

    #: The attachment ID
    uid = attr.ib(None, type=Optional[str])


@attr.s(cmp=False)
class UnsentMessage(Attachment):
    """Represents an unsent message attachment"""


@attr.s(cmp=False)
class ShareAttachment(Attachment):
    """Represents a shared item (eg. URL) that has been sent as a Facebook attachment"""

    #: ID of the author of the shared post
    author = attr.ib(None, type=Optional[str])
    #: Target URL
    url = attr.ib(None, type=Optional[str])
    #: Original URL if Facebook redirects the URL
    original_url = attr.ib(None, type=Optional[str])
    #: Title of the attachment
    title = attr.ib(None, type=Optional[str])
    #: Description of the attachment
    description = attr.ib(None, type=Optional[str])
    #: Name of the source
    source = attr.ib(None, type=Optional[str])
    #: URL of the attachment image
    image_url = attr.ib(None, type=Optional[str])
    #: URL of the original image if Facebook uses `safe_image`
    original_image_url = attr.ib(None, type=Optional[str])
    #: Width of the image
    image_width = attr.ib(None, type=Optional[int])
    #: Height of the image
    image_height = attr.ib(None, type=Optional[int])
    #: List of additional attachments
    attachments = attr.ib(
        factory=list, type=List[Attachment], converter=lambda x: [] if x is None else x
    )

    # Put here for backwards compatibility, so that the init argument order is preserved
    uid = attr.ib(None, type=Optional[str])
