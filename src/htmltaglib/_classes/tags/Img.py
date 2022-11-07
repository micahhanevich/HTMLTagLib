from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Img(Element):
    """Represents an HTML Img Element;
    Defines an image.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword alt: Str; Specifies an alternate text for an image. (default: None)
    :keyword crossorigin: Img.CrossOrigin; Allow images from third-party sites that allow cross-origin access to be used with canvas. (default: None)
    :keyword height: Float; Specifies the height of an image. (default: None)
    :keyword width: Float; Specifies the width of an image. (default: None)
    :keyword ismap: Bool; Specifies an image as a server-side image map. (default: False)
    :keyword loading: Img.Loading; Specifies whether a browser should load an image immediately or to defer loading of images until some conditions are met. (default: None)
    :keyword longdesc: Str; Specifies a URL to a detailed description of an image. (default: None)
    :keyword referrerpolicy: Img.ReferrerPolicy; Specifies which referrer information to use when fetching an image. (default: None)
    :keyword sizes: Str; Specifies image sizes for different page layouts. (default: None)
    :keyword src: Str; Specifies the path to the image. (default: None)
    :keyword srcset: List of Str; Specifies a list of image files to use in different situations. (default: None)
    :keyword usemap: Str; Specifies an image as a client-side image map. (default: None) """

    class CrossOrigin(CustomEnum):
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class Loading(CustomEnum):
        EAGER = 'eager'
        LAZY = 'lazy'

    class ReferrerPolicy(CustomEnum):
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_CROSS_ORIGIN = 'origin-when-cross-origin'
        SAME_ORIGIN = 'same-origin'
        STRICT_ORIGIN_CROSS_ORIGIN = 'strict-origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.alt: str = kwargs.get('alt', None)  # Specifies an alternate text for an image
        self.crossorigin: Img.CrossOrigin = kwargs.get('crossorigin',
                                                       None)  # Allow images from third-party sites that allow cross-origin access to be used with canvas
        self.height: float = kwargs.get('height', None)  # Specifies the height of an image
        self.width: float = kwargs.get('width', None)  # Specifies the width of an image
        self.ismap: bool = kwargs.get('ismap', False)  # Specifies an image as a server-side image map
        self.loading: Img.Loading = kwargs.get('loading',
                                               None)  # Specifies whether a browser should load an image immediately or to defer loading of images until some conditions are met
        self.longdesc: str = kwargs.get('longdesc', None)  # Specifies a URL to a detailed description of an image
        self.referrerpolicy: Img.Referrerpolicy = kwargs.get('referrerpolicy',
                                                             None)  # Specifies which referrer information to use when fetching an image
        self.sizes: str = kwargs.get('sizes', None)  # Specifies image sizes for different page layouts
        self.src: str = kwargs.get('src', None)  # Specifies the path to the image
        self.srcset: list[str] = kwargs.get('srcset',
                                            None)  # Specifies a list of image files to use in different situations
        self.usemap: str = kwargs.get('usemap', None)  # Specifies an image as a client-side image map

        if self.alt is not None: attr.setdefault('alt', self.alt)
        if self.crossorigin is not None and self.crossorigin in Img.CrossOrigin.__members__.values(): attr.setdefault(
            'crossorigin', Img.CrossOrigin[self.crossorigin.name])
        if self.height is not None: attr.setdefault('height', self.height)
        if self.width is not None: attr.setdefault('width', self.width)
        if self.ismap: attr.setdefault('ismap', None)
        if self.loading is not None and self.loading in Img.Loading.__members__.values(): attr.setdefault('loading',
                                                                                                          Img.Loading[
                                                                                                              self.loading.name])
        if self.longdesc is not None: attr.setdefault('longdesc', self.longdesc)
        if self.referrerpolicy is not None and self.referrerpolicy in Img.Referrerpolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', Img.Referrerpolicy[self.referrerpolicy])
        if self.sizes is not None: attr.setdefault('sizes', self.sizes)
        if self.src is not None: attr.setdefault('src', self.src)
        if self.srcset is not None: attr.setdefault('srcset', str(', '.join(self.srcset)))
        if self.usemap is not None:
            if self.usemap[0] != '#': self.usemap = '#' + str(self.usemap)
            attr.setdefault('usemap', self.usemap)

        super().__init__('img', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
