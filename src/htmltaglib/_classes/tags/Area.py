from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Area(Element):
    """Represents an HTML Area element;
    Defines an area inside an image map.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword alt: Str; Specifies an alternate text for the area. Required if the href attribute is present. (default: None)
    :keyword coords: Str; Specifies the coordinates of the area. (default: None)
    :keyword download: Str; Specifies that the target will be downloaded when a user clicks on the hyperlink. (default: None)
    :keyword href: Str; Specifies the hyperlink target for the area. (default: None)
    :keyword hreflang: Str; Specifies the language of the target URL. (default: None)
    :keyword media: Str; Specifies what media/device the target URL is optimized for. (default: None)
    :keyword referrerpolicy: Area.ReferrerPolicy; Specifies which referrer information to send with the link. (default: None)
    :keyword rel: Area.Rel; Specifies the relationship between the current document and the target URL. (default: None)
    :keyword shape: Area.Shape; Specifies the shape of the area. (default: None)
    :keyword target: Area.Target; Specifies where to open the target URL. (default: None)
    :keyword HTMLtype: Str; Specifies the media type of the target URL. (default: None) """

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
        HELP = 'help'
        LICENSE = 'license'
        NEXT = 'next'
        NOFOLLOW = 'nofollow'
        NOREFERRER = 'noreferrer'
        PREFETCH = 'prefetch'
        PREV = 'prev'
        SEARCH = 'search'
        TAG = 'tag'

    class Shape(CustomEnum):
        DEFAULT = 'default'
        RECTANGLE = 'rect'
        CIRCLE = 'circle'
        POLYGON = 'poly'

    class Target(CustomEnum):
        BLANK = '_blank'
        PARENT = '_parent'
        SELF = '_self'
        TOP = '_top'

    def __init__(self, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.alt: str = kwargs.get('alt',
                                   None)  # Specifies an alternate text for the area. Required if the href attribute is present
        self.coords: str = kwargs.get('coords', None)  # Specifies the coordinates of the area
        self.download: str = kwargs.get('download',
                                        None)  # Specifies that the target will be downloaded when a user clicks on the hyperlink
        self.href: str = kwargs.get('href', None)  # Specifies the hyperlink target for the area
        self.hreflang: str = kwargs.get('hreflang', None)  # Specifies the language of the target URL
        self.media: str = kwargs.get('media', None)  # Specifies what media/device the target URL is optimized for
        self.referrerpolicy: Area.ReferrerPolicy = kwargs.get('referrerpolicy',
                                                              None)  # Specifies which referrer information to send with the link
        self.rel: Area.Rel = kwargs.get('rel',
                                        None)  # Specifies the relationship between the current document and the target URL
        self.shape: Area.Shape = kwargs.get('shape', None)  # Specifies the shape of the area
        self.target: Area.Target = kwargs.get('target', None)  # Specifies where to open the target URL
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the media type of the target URL

        if self.alt is not None:
            attr.setdefault('alt', self.alt)
        elif self.href is not None:
            raise AttributeError('alt attribute is required if the href attribute is present.')
        if self.coords is not None: attr.setdefault('coords', self.coords)
        if self.download is not None: attr.setdefault('shape', self.shape)
        if self.href is not None: attr.setdefault('href', self.href)
        if self.hreflang is not None: attr.setdefault('hreflang', self.hreflang)
        if self.media is not None: attr.setdefault('media', self.media)
        if self.referrerpolicy is not None and self.referrerpolicy in Area.Referrerpolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', Area.Referrerpolicy[self.referrerpolicy.name])
        if self.rel is not None and self.rel in Area.Rel.__members__.values(): attr.setdefault('rel',
                                                                                               Area.Rel[self.rel.name])
        if self.shape is not None and self.shape in Area.Shape.__members__.values(): attr.setdefault('shape',
                                                                                                     Area.Shape[
                                                                                                         self.shape.name])
        if self.target is not None: attr.setdefault('target', self.target)
        if self.HTMLtype is not None: attr.setdefault('type', self.HTMLtype)

        super().__init__('area', attr=attr, html=html, end_tag=False)
