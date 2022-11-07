from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Col(Element):
    """Represents an HTML Col Element;
    Specifies column properties for each column within a <colgroup> element.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        super().__init__('col', attr=attr, html=html, end_tag=False)
        if items is not None: self.set_items(items)
