from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class HTML(Element):
    """Represents an HTML HTML Element;
    Defines the root of an HTML document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword xmlns: Str; Specifies the XML namespace attribute (If you need your content to conform to XHTML). (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        # Specifies the XML namespace attribute (If you need your content to conform to XHTML)
        self.xmlns: str = kwargs.get('xmlns', None)

        if self.xmlns is not None: attr.setdefault('xmlns', self.xmlns)

        super().__init__('html', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
