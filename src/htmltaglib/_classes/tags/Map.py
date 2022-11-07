from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Map(Element):
    """Represents an HTML Map Element;
    Defines an image map.

    :param name: Str; Required. Specifies the name of the image map.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None) """

    def __init__(self, name: str, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.name: str = name  # Required. Specifies the name of the image map

        attr.setdefault('name', self.name)

        super().__init__('map', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
