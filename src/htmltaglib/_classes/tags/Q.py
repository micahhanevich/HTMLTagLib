from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Q(Element):
    """Represents an HTML Q Element;
    Defines a short quotation.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword cite: Str; Specifies the source URL of the quote. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.cite: str = kwargs.get('cite', None)  # Specifies the source URL of the quote

        if self.cite is not None: attr.setdefault('cite', self.cite)

        super().__init__('q', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
