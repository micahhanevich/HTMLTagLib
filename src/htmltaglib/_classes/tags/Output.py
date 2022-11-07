from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Output(Element):
    """Represents an HTML Output Element;
    Defines the result of a calculation.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword HTMLfor: Str; Specifies the relationship between the result of the calculation, and the elements used in the calculation. (default: None)
    :keyword form: Str; Specifies which form the output element belongs to. (default: None)
    :keyword name: Str; Specifies a name for the output element. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.HTMLfor: str = kwargs.get('HTMLfor',
                                       None)  # Specifies the relationship between the result of the calculation, and the elements used in the calculation
        self.form: str = kwargs.get('form', None)  # Specifies which form the output element belongs to
        self.name: str = kwargs.get('name', None)  # Specifies a name for the output element

        if self.HTMLfor is not None: attr.setdefault('for', self.HTMLfor)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.name is not None: attr.setdefault('name', self.name)

        super().__init__('output', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
