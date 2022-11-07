from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class THead(Element):
    """Represents an HTML THead Element;
    Groups the header content in a table.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        super().__init__('thead', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
