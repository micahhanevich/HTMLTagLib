from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Option(Element):
    """Represents an HTML Option Element;
    Defines an option in a drop-down list.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword disabled: Bool; Specifies that an option should be disabled. (default: False)
    :keyword label: Str; Specifies a shorter label for an option. (default: None)
    :keyword selected: Bool; Specifies that an option should be pre-selected when the page loads. (default: False)
    :keyword value: Str; Specifies the value to be sent to a server. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that an option should be disabled
        self.label: str = kwargs.get('label', None)  # Specifies a shorter label for an option
        self.selected: bool = kwargs.get('selected', False)  # Specifies that an option should be pre-selected when the page loads
        self.value: any = kwargs.get('value', None)  # Specifies the value to be sent to a server

        if self.disabled: attr.setdefault('disabled', None)
        if self.label is not None: attr.setdefault('label', self.label)
        if self.selected: attr.setdefault('selected', None)
        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('option', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
