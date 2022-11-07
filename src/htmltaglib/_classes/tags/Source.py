from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Source(Element):
    """Represents an HTML Source Element;
    Defines multiple media resources for media elements (<video> and <audio>).

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword media: Str; Accepts any valid media query that would normally be defined in a CSS. (default: None)
    :keyword sizes: Str; Specifies image sizes for different page layouts. (default: None)
    :keyword src: Str; Required when source is used in audio and video. Specifies the URL of the media file. (default: None)
    :keyword srcset: Str; Required when <source> is used in <picture>. Specifies the URL of the image to use in different situations. (default: None)
    :keyword HTMLtype: Str; Specifies the MIME-type of the resource. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.media: str = kwargs.get('media',
                                     None)  # Accepts any valid media query that would normally be defined in a CSS
        self.sizes: str = kwargs.get('sizes', None)  # Specifies image sizes for different page layouts
        self.src: str = kwargs.get('src',
                                   None)  # Required when source is used in audio and video. Specifies the URL of the media file
        self.srcset: str = kwargs.get('srcset',
                                      None)  # Required when source is used in picture. Specifies the URL of the image to use in different situations
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the MIME-type of the resource

        if self.media is not None: attr.setdefault('media', self.media)
        if self.sizes is not None: attr.setdefault('sizes', self.sizes)
        if self.src is not None: attr.setdefault('src', self.src)
        if self.srcset is not None: attr.setdefault('srcset', self.srcset)
        if self.type is not None: attr.setdefault('type', self.type)

        super().__init__('source', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
