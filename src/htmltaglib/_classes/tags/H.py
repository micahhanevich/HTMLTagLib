from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class H(Element):
    """Represents Elements h1 through h6;
    Defines HTML headings.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword headertype: Int; Used to identify which header type to create. (default: 1) """

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        headertype: int = kwargs.get('headertype', 1)  # Used to identify which header type to create
        if headertype < 1:
            headertype = 1
        elif headertype > 6:
            headertype = 6

        super().__init__('h' + str(headertype), attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
