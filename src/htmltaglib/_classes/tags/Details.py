from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Details(Element):
    """Represents an HTML Details Element;
    Defines additional details that the user can view or hide.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword open: Bool; Specifies that the details should be visible (open) to the user. (default: False) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.open: bool = kwargs.get('open', False)  # Specifies that the details should be visible (open) to the user

        if self.open: attr.setdefault('open', None)

        super().__init__('details', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
