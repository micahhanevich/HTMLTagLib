from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Style(Element):
    """Represents an HTML Style Element;
    Defines style information for a document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword media: Str; Specifies what media/device the media resource is optimized for. (default: None)
    :keyword HTMLtype: Style.Type; Specifies the media type of the style tag. (default: None) """

    class Type(CustomEnum):
        TEXT_CSS = 'text/css'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.media: str = kwargs.get('media', None)  # Specifies what media/device the media resource is optimized for
        self.type: Style.Type = kwargs.get('HTMLtype', None)  # Specifies the media type of the <style> tag

        if self.media is not None: attr.setdefault('media', self.media)
        if self.type is not None and self.type in Style.Type.__members__.values(): attr.setdefault('type', Style.Type[
            self.type.name])

        super().__init__('style', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
