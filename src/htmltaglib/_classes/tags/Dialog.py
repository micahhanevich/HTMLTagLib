from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Dialog(Element):
    """Represents an HTML Dialog Element;
    Defines a dialog box or window.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword open: Bool; Specifies that the dialog element is active and that the user can interact with it. (default: False) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.open: bool = kwargs.get('open',
                                     False)  # Specifies that the dialog element is active and that the user can interact with it

        if self.open: attr.setdefault('open', None)

        super().__init__('dialog', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
