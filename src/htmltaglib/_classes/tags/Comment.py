from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Comment(Element):
    """Represents an HTML Comment Element;
    Defines a comment.

    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, items: list = None, **kwargs):
        html: str = kwargs.get('html', None)

        super().__init__('!--', html=html, end_tag=True)
        if items is not None: self.set_items(items)
