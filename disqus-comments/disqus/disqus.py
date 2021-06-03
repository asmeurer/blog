from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://disqus.com"


@dataclass
class Author:
    class Meta:
        name = "author"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_anonymous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isAnonymous",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://disqus.com/disqus-internals",
        }
    )


@dataclass
class Category:
    class Meta:
        name = "category"

    forum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDefault",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://disqus.com/disqus-internals",
        }
    )


@dataclass
class Post:
    class Meta:
        name = "post"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
            "max_length": 200,
        }
    )
    parent: Optional["Post.Parent"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    thread: Optional["Post.Thread"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    author: Optional[Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipAddress",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    created_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdAt",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_deleted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDeleted",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_approved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isApproved",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_flagged: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFlagged",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_spam: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSpam",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_highlighted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isHighlighted",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "id",
            "type": "Attribute",
            "namespace": "http://disqus.com/disqus-internals",
        }
    )

    @dataclass
    class Parent:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "max_length": 200,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://disqus.com/disqus-internals",
            }
        )

    @dataclass
    class Thread:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "max_length": 200,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://disqus.com/disqus-internals",
            }
        )


@dataclass
class Thread:
    class Meta:
        name = "thread"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
            "max_length": 200,
        }
    )
    forum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    category: Optional["Thread.Category"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipAddress",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    author: Optional[Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    created_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdAt",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isClosed",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    is_deleted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDeleted",
            "type": "Element",
            "namespace": "http://disqus.com",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "id",
            "type": "Attribute",
            "namespace": "http://disqus.com/disqus-internals",
        }
    )

    @dataclass
    class Category:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://disqus.com/disqus-internals",
            }
        )


@dataclass
class Disqus:
    class Meta:
        name = "disqus"
        namespace = "http://disqus.com"

    category: List[Category] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    thread: List[Thread] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    post: List[Post] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
