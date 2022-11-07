from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class LI(Element):
    """Represents an HTML LI Element;
    Defines a list item.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword value: Int; Only for ol lists. Specifies the start value of a list item. The following list items will increment from that number. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.value: int = kwargs.get('value', None)

        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('li', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
