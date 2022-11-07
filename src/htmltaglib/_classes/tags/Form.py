from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Form(Element):
    """Represents an HTML Form Element;
    Defines an HTML form for user input.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword acceptcharset: Str; Specifies the character encodings that are to be used for the form submission. (default: None)
    :keyword action: Str; Specifies where to send the form-data when a form is submitted. (default: None)
    :keyword autocomplete: Bool; Specifies whether a form should have autocomplete on or off. (default: False)
    :keyword enctype: Form.EncType; Specifies how the form-data should be encoded when submitting it to the server (only for method="post"). (default: None)
    :keyword method: Form.Method; Specifies the HTTP method to use when sending form-data. (default: None)
    :keyword name: Str; Specifies the name of a form. (default: None)
    :keyword novalidate: Bool; Specifies that the form should not be validated when submitted. (default: False)
    :keyword rel: Form.Rel; Specifies the relationship between a linked resource and the current document. (default: None)
    :keyword target: Form.Target; Specifies where to display the response that is received after submitting the form. (default: None) """

    class EncType(CustomEnum):
        APPLICATION = 'application/x-www-form-urlencoded'
        MULTIPART = 'multipart/form-data'
        TEXT = 'text/plain'

    class Method(CustomEnum):
        GET = 'get'
        POST = 'post'

    class Rel(CustomEnum):
        EXTERNAL = 'external'
        HELP = 'help'
        LICENSE = 'license'
        NEXT = 'next'
        NOFOLLOW = 'nofollow'
        NOOPENER = 'noopener'
        NOREFERRER = 'noreferrer'
        OPENER = 'opener'
        PREV = 'prev'
        SEARCH = 'search'

    class Target(CustomEnum):
        BLANK = '_blank'
        PARENT = '_parent'
        SELF = '_self'
        TOP = '_top'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.acceptcharset: str = kwargs.get('acceptcharset', None)  # Specifies the character encodings that are to be used for the form submission
        self.action: str = kwargs.get('action', None)  # Specifies where to send the form-data when a form is submitted
        self.autocomplete: bool = kwargs.get('autocomplete', False)  # Specifies whether a form should have autocomplete on or off
        self.enctype: Form.EncType = kwargs.get('enctype', None)  # Specifies how the form-data should be encoded when submitting it to the server (only for method="post")
        self.method: Form.Method = kwargs.get('method', None)  # Specifies the HTTP method to use when sending form-data
        self.name: str = kwargs.get('name', None)  # Specifies the name of a form
        self.novalidate: bool = kwargs.get('novalidate', False)  # Specifies that the form should not be validated when submitted
        self.rel: Form.Rel = kwargs.get('rel', None)  # Specifies the relationship between a linked resource and the current document
        self.target: Form.Target = kwargs.get('target', None)  # Specifies where to display the response that is received after submitting the form

        if self.acceptcharset is not None: attr.setdefault('accept-charset', self.acceptcharset)
        if self.action is not None: attr.setdefault('action', self.action)
        if self.autocomplete and self.autocomplete is not None:
            attr.setdefault('autocomplete', 'on')
        elif not self.autocomplete and self.autocomplete is not None:
            attr.setdefault('autocomplete', 'off')
        if self.enctype is not None and self.enctype in Form.EncType.__members__.values(): attr.setdefault('enctype', Form.EncType[self.enctype.name])
        if self.method is not None and self.method in Form.Method.__members__.values(): attr.setdefault('method', Form.Method[self.method.name])
        if self.name is not None: attr.setdefault('name', self.name)
        if self.novalidate: attr.setdefault('novalidate', None)
        if self.rel is not None and self.rel in Form.Rel.__members__.values(): attr.setdefault('rel', Form.Rel[self.rel.name])
        if self.target is not None and self.target in Form.Target.__members__.values(): attr.setdefault('target', Form.Target[self.target.name])

        super().__init__('form', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
