from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Ins(Element):
    """Represents an HTML Ins Element;
    Defines a text that has been inserted into a document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword cite: Specifies a URL to a document that explains the reason why the text was inserted/changed. (default: None)
    :keyword datetime: Specifies a URL to a document that explains the reason why the text was inserted/changed. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.cite: str = kwargs.get('cite',
                                    None)  # Specifies a URL to a document that explains the reason why the text was inserted/changed
        self.datetime: str = kwargs.get('datetime',
                                        None)  # Specifies a URL to a document that explains the reason why the text was inserted/changed

        super().__init__('ins', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
