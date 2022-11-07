from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Del(Element):
    """Represents an HTML Del Element;
    Defines text that has been deleted from a document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword cite: Str; Specifies a URL to a document that explains the reason why the text was deleted/changed. (default: None)
    :keyword datetime: Datetime; Specifies the date and time of when the text was deleted/changed. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.cite: str = kwargs.get('cite', None)
        self.datetime: datetime = kwargs.get('datetime', None)

        if self.cite is not None: attr.setdefault('cite',
                                                  self.cite)  # Specifies a URL to a document that explains the reason why the text was deleted/changed
        if self.datetime is not None: attr.setdefault('datetime', repr(
            self.datetime))  # Specifies the date and time of when the text was deleted/changed

        super().__init__('del', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
