from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Base(Element):
    """Represents an HTML Base element;
    Specifies the base URL/target for all relative URLs in a document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword href: Str; Specifies the base URL for all relative URLs in the page. (default: None)
    :keyword target: Base.Target; Specifies the default target for all hyperlinks and forms in the page. (default: None) """

    class Target(CustomEnum):
        BLANK = '_blank'
        PARENT = '_parent'
        SELF = '_self'
        TOP = '_top'

    def __init__(self, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.href: str = kwargs.get('href', None)  # Specifies the base URL for all relative URLs in the page
        self.target: Base.Target = kwargs.get('target',
                                              None)  # Specifies the default target for all hyperlinks and forms in the page

        if self.href is not None: attr.setdefault('href', self.href)
        if self.target is not None and self.target in Base.Target.__members__.values(): attr.setdefault(
            'target', Base.Target[self.target.name])

        super().__init__('base', attr=attr, html=html, end_tag=True)
