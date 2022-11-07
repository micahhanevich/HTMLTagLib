from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Fieldset(Element):
    """Represents an HTML Fieldset Element;
    Groups related elements in a form.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword disabled: Bool; Specifies that a group of related form elements should be disabled. (default: False)
    :keyword form: Str; Specifies which form the fieldset belongs to. (default: None)
    :keyword name: Str; Specifies a name for the fieldset. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.disabled: bool = kwargs.get('disabled',
                                         False)  # Specifies that a group of related form elements should be disabled
        self.form: str = kwargs.get('form', None)  # Specifies which form the fieldset belongs to
        self.name: str = kwargs.get('name', None)  # Specifies a name for the fieldset

        if self.disabled: attr.setdefault('disabled', None)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.name is not None: attr.setdefault('name', self.name)

        super().__init__('fieldset', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
