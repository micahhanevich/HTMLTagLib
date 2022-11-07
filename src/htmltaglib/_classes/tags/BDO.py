from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class BDO(Element):
    """Represents an HTML Bdo element;
    Overrides the current text direction.

    :param HTMLdir: BDO.Direction; Required. Specifies the text direction of the text inside the bdo element. (default: BDO.Direction.LEFT_TO_RIGHT)

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None) """

    class Direction(CustomEnum):
        LEFT_TO_RIGHT = 'ltr'
        RIGHT_TO_LEFT = 'rtl'

    def __init__(self, HTMLdir: Direction, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.HTMLdir = HTMLdir  # Required. Specifies the text direction of the text inside the <bdo> element

        # Specifies the text direction of the text inside the <bdo> element
        if self.HTMLdir is not None and self.HTMLdir in BDO.Direction: attr.setdefault('dir',
                                                                                       BDO.Direction[self.HTMLdir.name])

        super().__init__('bdo', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
