from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Progress(Element):
    """Represents an HTML Progress Element;
    Represents the progress of a task.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword max: Float; Specifies how much work the task requires in total. Default value is 1. (default: 1.0)
    :keyword value: Float; Specifies how much of the task has been completed. (default: None) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.max: float = kwargs.get('max',
                                     1.0)  # Specifies how much work the task requires in total. Default value is 1
        self.value: float = kwargs.get('value', None)  # Specifies how much of the task has been completed

        if self.max is not None: attr.setdefault('max', self.max)
        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('progress', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
