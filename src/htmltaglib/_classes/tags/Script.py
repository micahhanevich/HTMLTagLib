from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Script(Element):
    """Represents an HTML Script Element;
    Defines a client-side script.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword htmlasync: Bool; Specifies that the script is downloaded in parallel to parsing the page, and executed as soon as it is available (before parsing completes) (only for external scripts). (default: False)
    :keyword crossorigin: Script.CrossOrigin; Sets the mode of the request to an HTTP CORS Request. (default: None)
    :keyword defer: Bool; Specifies that the script is downloaded in parallel to parsing the page, and executed after the page has finished parsing (only for external scripts). (default: False)
    :keyword integrity: Str; Allows a browser to check the fetched script to ensure that the code is never loaded if the source has been manipulated. (default: None)
    :keyword nomodule: Bool; Specifies that the script should not be executed in browsers supporting ES2015 modules. (default: None)
    :keyword referrerpolicy: Script.ReferrerPolicy; Specifies which referrer information to send when fetching a script. (default: None)
    :keyword src: Str; Specifies the URL of an external script file. (default: None)
    :keyword HTMLtype: Str; Specifies the media type of the script. (default: None) """

    class CrossOrigin(CustomEnum):
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class ReferrerPolicy(CustomEnum):
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_CROSS_ORIGIN = 'origin-when-cross-origin'
        SAME_ORIGIN = 'same-origin'
        STRICT_ORIGIN = 'strict-origin'
        STRICT_ORIGIN_CROSS_ORIGIN = 'strict-origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.htmlasync: bool = kwargs.get('HTMLasync',
                                          False)  # Specifies that the script is downloaded in parallel to parsing the page, and executed as soon as it is available (before parsing completes) (only for external scripts)
        self.crossorigin: Script.CrossOrigin = kwargs.get('crossorigin',
                                                          None)  # Sets the mode of the request to an HTTP CORS Request
        self.defer: bool = kwargs.get('defer',
                                      False)  # Specifies that the script is downloaded in parallel to parsing the page, and executed after the page has finished parsing (only for external scripts)
        self.integrity: str = kwargs.get('integrity',
                                         None)  # Allows a browser to check the fetched script to ensure that the code is never loaded if the source has been manipulated
        self.nomodule: bool = kwargs.get('nomodule',
                                         None)  # Specifies that the script should not be executed in browsers supporting ES2015 modules
        self.referrerpolicy: Script.ReferrerPolicy = kwargs.get('referrerpolicy',
                                                                None)  # Specifies which referrer information to send when fetching a script
        self.src: str = kwargs.get('src', None)  # Specifies the URL of an external script file
        self.HTMLtype: str = kwargs.get('HTMLtype', None)  # Specifies the media type of the script

        if self.htmlasync: attr.setdefault('async', None)
        if self.crossorigin is not None and self.crossorigin in Script.CrossOrigin.__members__.values(): attr.setdefault(
            'crossorigin', Script.CrossOrigin[self.crossorigin.name])
        if self.defer: attr.setdefault('defer', None)
        if self.integrity is not None: attr.setdefault('integrity', self.integrity)
        if self.nomodule is not None: attr.setdefault('nomodule', self.nomodule)
        if self.referrerpolicy is not None and self.referrerpolicy in Script.ReferrerPolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', Script.ReferrerPolicy[self.referrerpolicy.name])
        if self.src is not None: attr.setdefault('src', self.src)
        if self.HTMLtype is not None: attr.setdefault('type', self.HTMLtype)

        super().__init__('script', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
