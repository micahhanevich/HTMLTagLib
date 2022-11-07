from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class I(Element):
    """Represents an HTML I Element;
    Defines a part of text in an alternate voice or mood.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        super().__init__('i', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
