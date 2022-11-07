from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Object(Element):
    """Represents an HTML Object Element;
    Defines a container for an external application.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword data: Str; Specifies the URL of the resource to be used by the object. (default: None)
    :keyword form: Str; Specifies which form the object belongs to. (default: None)
    :keyword height: Float; Specifies the height of the object. (default: None)
    :keyword width: Float; Specifies the width of the object. (default: None)
    :keyword name: Str; Specifies a name for the object. (default: None)
    :keyword HTMLtype: Str; Specifies the media type of data specified in the data attribute. (default: None)
    :keyword typemustmatch: Bool; Specifies whether the type attribute and the actual content of the resource must match to be displayed. (default: None)
    :keyword usemap: Str; Specifies the name of a client-side image map to be used with the object. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.data: str = kwargs.get('data', None)  # Specifies the URL of the resource to be used by the object
        self.form: str = kwargs.get('form', None)  # Specifies which form the object belongs to
        self.height: float = kwargs.get('height', None)  # Specifies the height of the object
        self.width: float = kwargs.get('width', None)  # Specifies the width of the object
        self.name: str = kwargs.get('name', None)  # Specifies a name for the object
        self.HTMLtype: str = kwargs.get('HTMLtype',
                                        None)  # Specifies the media type of data specified in the data attribute
        self.typemustmatch: bool = kwargs.get('typemustmatch',
                                              None)  # Specifies whether the type attribute and the actual content of the resource must match to be displayed
        self.usemap: str = kwargs.get('usemap',
                                      None)  # Specifies the name of a client-side image map to be used with the object

        if self.data is not None: attr.setdefault('data', self.data)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.height is not None: attr.setdefault('height', self.height)
        if self.width is not None: attr.setdefault('width', self.width)
        if self.name is not None: attr.setdefault('name', self.name)
        if self.type is not None: attr.setdefault('type', self.type)
        if self.typemustmatch is not None: attr.setdefault('typemustmatch', self.typemustmatch)
        if self.usemap is not None: attr.setdefault('usemap', self.usemap) if self.usemap[
                                                                                  0] == '#' else attr.setdefault(
            'usemap', '#' + self.usemap)

        super().__init__('object', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
