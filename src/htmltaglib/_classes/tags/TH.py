from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class TH(Element):
    """Represents an HTML TH Element;
    Defines a header cell in a table.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword abbr: Str; Specifies an abbreviated version of the content in a header cell. (default: None)
    :keyword colspan: Int; Specifies the number of columns a header cell should span. (default: None)
    :keyword headers: Str; Specifies one or more header cells a cell is related to. (default: None)
    :keyword rowspan: Int; Specifies the number of rows a header cell should span. (default: None)
    :keyword scope: TH.Scope; Specifies whether a header cell is a header for a column, row, or group of columns or rows. (default: None) """

    class Scope(CustomEnum):
        COL = 'col'
        COLGROUP = 'colgroup'
        ROW = 'row'
        ROWGROUP = 'rowgroup'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.abbr: str = kwargs.get('abbr', None)  # Specifies an abbreviated version of the content in a header cell
        self.colspan: int = kwargs.get('colspan', None)  # Specifies the number of columns a header cell should span
        self.headers: str = kwargs.get('headers', None)  # Specifies one or more header cells a cell is related to
        self.rowspan: int = kwargs.get('rowspan', None)  # Specifies the number of rows a header cell should span
        self.scope: TH.Scope = kwargs.get('scope',
                                          None)  # Specifies whether a header cell is a header for a column, row, or group of columns or rows

        if self.abbr is not None: attr.setdefault('abbr', self.abbr)
        if self.colspan is not None: attr.setdefault('colspan', self.colspan)
        if self.headers is not None: attr.setdefault('headers', self.headers)
        if self.rowspan is not None: attr.setdefault('rowspan', self.rowspan)
        if self.scope is not None and self.scope in TH.Scope.__members__.values(): attr.setdefault('scope', TH.Scope[
            self.scope.name])

        super().__init__('th', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
