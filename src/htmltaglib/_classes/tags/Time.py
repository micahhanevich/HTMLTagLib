from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Time(Element):
    """Represents an HTML Time Element;
    Defines a specific time (or datetime).

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword datetime: Str; Represents a machine-readable format of the time element. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.datetime: str = kwargs.get('datetime', None)  # Represents a machine-readable format of the <time> element

        if self.datetime is not None: attr.setdefault('datetime', self.datetime)

        super().__init__('time', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
