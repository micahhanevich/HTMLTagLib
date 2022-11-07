from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Small(Element):
    """Represents an HTML Small Element;
    Defines smaller text.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        super().__init__('small', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
