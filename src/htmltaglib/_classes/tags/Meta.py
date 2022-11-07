from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Meta(Element):
    """Represents an HTML Meta Element;
    Defines metadata about an HTML document.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword charset: Str; Specifies the character encoding for the HTML document. (default: None)
    :keyword content: Str; Specifies the value associated with the http-equiv or name attribute. (default: None)
    :keyword httpequiv: Meta.HttpEquiv; Provides an HTTP header for the information/value of the content attribute. (default: None)
    :keyword name: Meta.Name; Specifies a name for the metadata. (default: None) """

    class HttpEquiv(CustomEnum):
        CONTENT_SEC_POLICY = 'content-security-policy'
        CONTENT_TYPE = 'content-type'
        DEFAULT_STYLE = 'default-style'
        REFRESH = 'refresh'

    class Name(CustomEnum):
        APPLICATION_NAME = 'application-name'
        AUTHOR = 'author'
        DESCRIPTION = 'description'
        GENERATOR = 'generator'
        KEYWORDS = 'keywords'
        VIEWPORT = 'viewport'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.charset: str = kwargs.get('charset', None)  # Specifies the character encoding for the HTML document
        self.content: str = kwargs.get('content',
                                       None)  # Specifies the value associated with the http-equiv or name attribute
        self.httpequiv: Meta.HttpEquiv = kwargs.get('httpequiv',
                                                    None)  # Provides an HTTP header for the information/value of the content attribute
        self.name: Meta.Name = kwargs.get('name', None)  # Specifies a name for the metadata

        if self.charset is not None: attr.setdefault('charset', self.charset)
        if self.content is not None: attr.setdefault('content', self.content)
        if self.httpequiv is not None and self.httpequiv in Meta.HttpEquiv.__members__.values(): attr.setdefault(
            'httpequiv', Meta.HttpEquiv[self.httpequiv.name])
        if self.name is not None and self.name in Meta.Name.__members__.values(): attr.setdefault('name', Meta.Name[
            self.Name.name])

        super().__init__('meta', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
