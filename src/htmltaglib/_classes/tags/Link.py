from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Link(Element):
    """Represents an HTML Link Element;
    Defines the relationship between a document and an external resource (most used to link to style sheets).

    :param rel: Link.Rel; Required. Specifies the relationship between the current document and the linked document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword crossorigin: Link.CrossOrigin; Specifies how the element handles cross-origin requests. (default: None)
    :keyword href: Str; Specifies the location of the linked document. (default: None)
    :keyword hreflang: Str; Specifies the language of the text in the linked document. (default: None)
    :keyword media: Str; Specifies on what device the linked document will be displayed. (default: None)
    :keyword referrerpolicy: Link.ReferrerPolicy; Specifies which referrer to use when fetching the resource. (default: None)
    :keyword sizes: Str; Specifies the size of the linked resource. Only for rel="icon". (default: None)
    :keyword HTMLtype: Str; Specifies the media type of the linked document. (default: None) """

    class CrossOrigin(CustomEnum):
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class ReferrerPolicy(CustomEnum):
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_CROSS_ORIGIN = 'origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    class Rel(CustomEnum):
        ALTERNATE = 'alternate'
        AUTHOR = 'author'
        DNS_PREFETCH = 'dns_prefetch'
        HELP = 'help'
        ICON = 'icon'
        LICENSE = 'license'
        NEXT = 'next'
        PINGBACK = 'pingback'
        PRECONNECT = 'preconnect'
        PREFETCH = 'prefetch'
        PRELOAD = 'preload'
        PRERENDER = 'prerender'
        PREV = 'prev'
        SEARCH = 'search'
        STYLESHEET = 'stylesheet'

    def __init__(self, rel: Rel, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.crossorigin: Link.CrossOrigin = kwargs.get('crossorigin',
                                                        None)  # Specifies how the element handles cross-origin requests
        self.href: str = kwargs.get('href', None)  # Specifies the location of the linked document
        self.hreflang: str = kwargs.get('hreflang', None)  # Specifies the language of the text in the linked document
        self.media: str = kwargs.get('media', None)  # Specifies on what device the linked document will be displayed
        self.referrerpolicy: Link.ReferrerPolicy = kwargs.get('referrerpolicy',
                                                              None)  # Specifies which referrer to use when fetching the resource
        self.rel: Link.Rel = rel  # Required. Specifies the relationship between the current document and the linked document
        self.sizes: str = kwargs.get('sizes', None)  # Specifies the size of the linked resource. Only for rel="icon"
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the media type of the linked document

        if self.crossorigin is not None and self.crossorigin in Link.CrossOrigin.__members__.values(): attr.setdefault(
            'crossorigin', Link.CrossOrigin[self.crossorigin.name])
        if self.href is not None: attr.setdefault('href', self.href)
        if self.hreflang is not None: attr.setdefault('hreflang', self.hreflang)
        if self.media is not None: attr.setdefault('media', self.media)
        if self.referrerpolicy is not None and self.referrerpolicy in Link.ReferrerPolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', Link.ReferrerPolicy[self.referrerpolicy.name])
        if self.rel is not None and self.rel in Link.Rel.__members__.values(): attr.setdefault('rel', Link.Rel[self.rel.name])
        if self.sizes is not None: attr.setdefault('sizes', self.sizes)
        if self.HTMLtype is not None: attr.setdefault('type', self.type)

        super().__init__('link', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
