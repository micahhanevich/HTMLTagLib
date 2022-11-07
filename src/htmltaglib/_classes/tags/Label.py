from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Label(Element):
    """Represents an HTML Label Element;
    Defines a label for an input element.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword HTMLfor: Str; Specifies the id of the form element the label should be bound to. (default: None)
    :keyword form: Str; Specifies which form the label belongs to. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.HTMLfor: str = kwargs.get('HTMLfor', None)  # Specifies the id of the form element the label should be bound to
        self.form: str = kwargs.get('form', None)  # Specifies which form the label belongs to

        if self.HTMLfor is not None: attr.setdefault('for', self.HTMLfor)
        if self.form is not None: attr.setdefault('form', self.form)

        super().__init__('label', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
