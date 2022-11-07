from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class OptGroup(Element):
    """Represents an HTML OptGroup Element;
    Defines a group of related options in a drop-down list.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword disabled: Bool; Specifies that an option-group should be disabled. (default: False)
    :keyword label: Str; Specifies a label for an option-group. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that an option-group should be disabled
        self.label: str = kwargs.get('label', None)  # Specifies a label for an option-group

        if self.disabled: attr.setdefault('disabled', None)
        if self.label is not None: attr.setdefault('label', self.label)

        super().__init__('optgroup', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
