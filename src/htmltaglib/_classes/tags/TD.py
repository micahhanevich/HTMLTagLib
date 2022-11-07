from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class TD(Element):
    """Represents an HTML TD Element;
    Defines a cell in a table.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword colspan: Int; Specifies the number of columns a cell should span. (default: None)
    :keyword headers: Str; Specifies one or more header cells a cell is related to. (default: None)
    :keyword rowspan: Int; Sets the number of rows a cell should span. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.colspan: int = kwargs.get('colspan', None)  # Specifies the number of columns a cell should span
        self.headers: str = kwargs.get('headers', None)  # Specifies one or more header cells a cell is related to
        self.rowspan: int = kwargs.get('rowspan', None)  # Sets the number of rows a cell should span

        if self.colspan is not None: attr.setdefault('colspan', self.colspan)
        if self.headers is not None: attr.setdefault('headers', self.headers)
        if self.rowspan is not None: attr.setdefault('rowspan', self.rowspan)

        super().__init__('td', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
