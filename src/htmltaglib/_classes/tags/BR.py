from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class BR(Element):
    """Represents an HTML br element;
    Defines a single line break.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)"""

    def __init__(self, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        super().__init__('br', attr=attr, html=html, end_tag=False)
