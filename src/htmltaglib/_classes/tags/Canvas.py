from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Canvas(Element):
    """Represents an HTML Canvas Element;
    Used to draw graphics, on the fly, via scripting (usually JavaScript).

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword height: Float; Specifies the height of the canvas. Default value is 150. (default: None)
    :keyword width: Float; Specifies the width of the canvas Default value is 300. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.height: float = kwargs.get('height', None)  # Specifies the height of the canvas. Default value is 150
        self.width: float = kwargs.get('width', None)  # Specifies the width of the canvas Default value is 300

        if self.height is not None: attr.setdefault('height', str(self.height) + 'px')
        if self.width is not None: attr.setdefault('width', str(self.width) + 'px')

        super().__init__('canvas', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
