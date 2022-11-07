from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Embed(Element):
    """Represents an HTML Embed Element;
    Defines a container for an external application.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword height: Float; Specifies the height of the embedded content. (default: None)
    :keyword width: Float; Specifies the width of the embedded content. (default: None)
    :keyword src: Str; Specifies the media type of the embedded content. (default: None)
    :keyword HTMLtype: Str; Specifies the address of the external file to embed. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.height: float = kwargs.get('height', None)  # Specifies the height of the embedded content
        self.width: float = kwargs.get('width', None)  # Specifies the width of the embedded content
        self.src: str = kwargs.get('src', None)  # Specifies the media type of the embedded content
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the address of the external file to embed

        if self.height is not None: attr.setdefault('height', str(self.height))
        if self.width is not None: attr.setdefault('width', str(self.width))
        if self.src is not None: attr.setdefault('src', str(self.src))
        if self.HTMLtype is not None: attr.setdefault('type', str(self.type))

        super().__init__('embed', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
