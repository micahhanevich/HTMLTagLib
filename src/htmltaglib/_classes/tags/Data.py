from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Data(Element):
    """Represents an HTML Data Element;
    Adds a machine-readable translation of a given content.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword value: Str; Specifies the machine-readable translation of the content of the element. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.value: str = kwargs.get('value',
                                     None)  # Specifies the machine-readable translation of the content of the element

        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('data', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
