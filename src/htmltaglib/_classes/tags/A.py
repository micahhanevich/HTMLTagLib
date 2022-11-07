from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class A(Element):
    """ Represents an HTML a element;
    Defines a hyperlink

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword download: Str; Specifies that the target will be downloaded when a user clicks on the hyperlink. (default: None)
    :keyword href: Str; Specifies the URL of the page the link goes to. (default: None)
    :keyword hreflang: Str; Specifies the language of the linked document. (default: None)
    :keyword media: Str; Specifies what media/device the linked document is optimized for. (default: None)
    :keyword ping: List of Str; Specifies a space-separated list of URLs to which, when the link is followed, post requests with the body ping will be sent by the browser (in the background). Typically used for tracking. (default: None)
    :keyword referrerpolicy: A.ReferrerPolicy; Specifies which referrer information to send with the link. (default: None)
    :keyword rel: A.Rel; Specifies the relationship between the current document and the linked document. (default: None)
    :keyword target: A.Target; Specifies where to open the linked document. (default: None)
    :keyword HTMLtype: Str; Specifies the media type of the linked document (default: None) """

    class ReferrerPolicy(CustomEnum):
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_CROSS_ORIGIN = 'origin-when-cross-origin'
        SAME_ORIGIN = 'same-origin'
        STRICT_ORIGIN_CROSS_ORIGIN = 'strict-origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    class Rel(CustomEnum):
        ALTERNATE = 'alternate'
        AUTHOR = 'author'
        BOOKMARK = 'bookmark'
        EXTERNAL = 'external'
        HELP = 'help'
        LICENSE = 'license'
        NEXT = 'next'
        NOFOLLOW = 'nofollow'
        NOREFERRER = 'noreferrer'
        NOOPENER = 'noopener'
        PREV = 'prev'
        SEARCH = 'search'
        TAG = 'tag'

    class Target(CustomEnum):
        BLANK = '_blank'
        PARENT = '_parent'
        SELF = '_self'
        TOP = '_top'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.download: str = kwargs.get('download',
                                        None)  # Specifies that the target will be downloaded when a user clicks on the hyperlink
        self.href: str = kwargs.get('href', None)  # Specifies the URL of the page the link goes to
        self.hreflang: str = kwargs.get('hreflang', None)  # Specifies the language of the linked document
        self.media: str = kwargs.get('media', None)  # Specifies what media/device the linked document is optimized for

        # Specifies a space-separated list of URLs to which, when
        # the link is followed, post requests with the body ping
        # will be sent by the browser (in the background). Typically used for tracking.
        self.ping: list[str] = kwargs.get('ping', None)
        self.referrerpolicy: A.ReferrerPolicy = kwargs.get('referrerpolicy',
                                                           None)  # Specifies which referrer information to send with the link
        self.rel: A.Rel = kwargs.get('rel',
                                     None)  # Specifies the relationship between the current document and the linked document
        self.target: A.Target = kwargs.get('target', None)  # Specifies where to open the linked document
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the media type of the linked document

        if self.download is not None: attr.setdefault('download', self.download)
        if self.href is not None: attr.setdefault('href', self.href)
        if self.hreflang is not None: attr.setdefault('hreflang', self.hreflang)
        if self.media is not None: attr.setdefault('media', self.media)
        if self.ping is not None: attr.setdefault('ping', ' '.join(self.ping))
        if self.referrerpolicy is not None and self.referrerpolicy in A.Referrerpolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', A.Referrerpolicy[self.referrerpolicy.name])
        if self.rel is not None and self.rel in A.Rel.__members__.values(): attr.setdefault('rel', A.Rel[self.rel.name])
        if self.target is not None and self.target in A.Target.__members__.values(): attr.setdefault(
            'target', A.Target[self.target.name])
        if self.HTMLtype is not None: attr.setdefault('type', self.HTMLtype)

        super().__init__('a', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
