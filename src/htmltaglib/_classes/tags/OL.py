from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class OL(Element):
    """Represents an HTML OL Element;
    Defines an ordered list.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword reversed: Bool; Specifies that the list order should be reversed (9,8,7...). (default: False)
    :keyword start: Float; Specifies the start value of an ordered list. (default: None)
    :keyword HTMLtype: OL.Type; Specifies the kind of marker to use in the list. (default: OL.Type.DECIMAL) """

    class Type(CustomEnum):
        DECIMAL = '1'  # Default. Decimal numbers (1, 2, 3, 4)
        ALPHA_LOWERCASE = 'a'  # Alphabetically ordered list, lowercase (a, b, c, d)
        ALPHA_UPPERCASE = 'A'  # Alphabetically ordered list, uppercase (A, B, C, D)
        ROMAN_LOWERCASE = 'i'  # Roman numbers, lowercase (i, ii, iii, iv)
        ROMAN_UPPERCASE = 'I'  # Roman numbers, uppercase (I, II, III, IV)

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.reversed: bool = kwargs.get('reversed',
                                         False)  # Specifies that the list order should be reversed (9,8,7...)
        self.start: float = kwargs.get('start', None)  # Specifies the start value of an ordered list
        self.type: OL.Type = kwargs.get('HTMLtype', OL.Type.DECIMAL)  # Specifies the kind of marker to use in the list

        if self.reversed: attr.setdefault('reversed', None)
        if self.start is not None: attr.setdefault('start', self.start)
        if self.type is not None and self.type in OL.Type.__members__.values(): attr.setdefault('type',
                                                                                                OL.Type[self.type.name])

        super().__init__('ol', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
