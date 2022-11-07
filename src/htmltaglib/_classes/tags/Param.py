from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Param(Element):
    """Represents an HTML Param Element;
    Defines a parameter for an object.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword name: Str; Specifies the name of a parameter. (default: None)
    :keyword value: Str; Specifies the value of the parameter. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.name: str = kwargs.get('name', None)  # Specifies the name of a parameter
        self.value: str = kwargs.get('value', None)  # Specifies the value of the parameter

        if self.name is not None: attr.setdefault('name', self.name)
        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('param', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
