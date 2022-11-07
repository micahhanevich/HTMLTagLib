from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Select(Element):
    """Represents an HTML Select Element;
    Defines a drop-down list.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword autofocus: Bool; Specifies that the drop-down list should automatically get focus when the page loads. (default: False)
    :keyword disabled: Bool; Specifies that a drop-down list should be disabled. (default: False)
    :keyword form: Str; Defines which form the drop-down list belongs to. (default: None)
    :keyword multiple: Bool; Specifies that multiple options can be selected at once. (default: False)
    :keyword name: Str; Defines a name for the drop-down list. (default: None)
    :keyword required: Bool; Specifies that the user is required to select a value before submitting the form. (default: False)
    :keyword size: Int; Defines the number of visible options in a drop-down list. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.autofocus: bool = kwargs.get('autofocus',
                                          False)  # Specifies that the drop-down list should automatically get focus when the page loads
        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that a drop-down list should be disabled
        self.form: str = kwargs.get('form', None)  # Defines which form the drop-down list belongs to
        self.multiple: bool = kwargs.get('multiple', False)  # Specifies that multiple options can be selected at once
        self.name: str = kwargs.get('name', None)  # Defines a name for the drop-down list
        self.required: bool = kwargs.get('required',
                                         False)  # Specifies that the user is required to select a value before submitting the form
        self.size: int = kwargs.get('size', None)  # Defines the number of visible options in a drop-down list

        if self.autofocus: attr.setdefault('autofocus', None)
        if self.disabled: attr.setdefault('disabled', None)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.multiple: attr.setdefault('multiple', None)
        if self.name is not None: attr.setdefault('name', self.name)
        if self.required: attr.setdefault('required', None)
        if self.size is not None: attr.setdefault('size', self.size)

        super().__init__('select', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
