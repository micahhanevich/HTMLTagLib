from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class IFrame(Element):
    """Represents an HTML IFrame Element;
    Defines an inline frame.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword allowfullscreen: Bool; Set to true if the <iframe> can activate fullscreen mode by calling the requestFullscreen() method. (default: None)
    :keyword allowpaymentrequest: Bool; Set to true if a cross-origin <iframe> should be allowed to invoke the Payment Request API. (default: None)
    :keyword height: Float; Specifies the height of an <iframe>. Default height is 150 pixels. (default: None)
    :keyword width: Float; Specifies the width of an <iframe>. Default width is 300 pixels. (default: None)
    :keyword loading: IFrame.Loading; Specifies whether a browser should load an iframe immediately or to defer loading of iframes until some conditions are met. (default: None)
    :keyword name: Str; Specifies the name of an <iframe>. (default: None)
    :keyword referrerpolicy: IFrame.ReferrerPolicy; Specifies which referrer information to send when fetching the iframe. (default: None)
    :keyword sandbox: IFrame.Sandbox; Enables an extra set of restrictions for the content in an <iframe>. (default: None)
    :keyword src: Str; Specifies the address of the document to embed in the <iframe>. (default: None)
    :keyword srcdoc: Str; Specifies the HTML content of the page to show in the <iframe>. (default: None) """

    class Loading(CustomEnum):
        EAGER = 'eager'
        LAZY = 'lazy'

    class ReferrerPolicy(CustomEnum):
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_CROSS_ORIGIN = 'origin-when-cross-origin'
        SAME_ORIGIN = 'same-origin'
        STRICT_ORIGIN_CROSS_ORIGIN = 'strict-origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    class Sandbox(CustomEnum):
        ALLOW_FORMS = 'allow-forms'
        ALLOW_POINTER_LOCK = 'allow-pointer-lock'
        ALLOW_POPUPS = 'allow-popups'
        ALLOW_SAME_ORIGIN = 'allow-same-origin'
        ALLOW_SCRIPTS = 'allow-scripts'
        ALLOW_TOP_NAVIGATION = 'allow_top_navigation'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.allowfullscreen: bool = kwargs.get('allowfullscreen',
                                                None)  # Set to true if the <iframe> can activate fullscreen mode by calling the requestFullscreen() method
        self.allowpaymentrequest: bool = kwargs.get('allowpaymentrequest',
                                                    None)  # Set to true if a cross-origin <iframe> should be allowed to invoke the Payment Request API
        self.height: float = kwargs.get('height',
                                        None)  # Specifies the height of an <iframe>. Default height is 150 pixels
        self.width: float = kwargs.get('width', None)  # Specifies the width of an <iframe>. Default width is 300 pixels
        self.loading: IFrame.Loading = kwargs.get('loading',
                                                  None)  # Specifies whether a browser should load an iframe immediately or to defer loading of iframes until some conditions are met
        self.name: str = kwargs.get('name', None)  # Specifies the name of an <iframe>
        self.referrerpolicy: IFrame.ReferrerPolicy = kwargs.get('referrerpolicy',
                                                                None)  # Specifies which referrer information to send when fetching the iframe
        self.sandbox: IFrame.Sandbox = kwargs.get('sandbox',
                                                  None)  # Enables an extra set of restrictions for the content in an <iframe>
        self.src: str = kwargs.get('src', None)  # Specifies the address of the document to embed in the <iframe>
        self.srcdoc: str = kwargs.get('srcdoc', None)  # Specifies the HTML content of the page to show in the <iframe>

        if self.allowfullscreen is not None and self.allowfullscreen:
            attr.setdefault('allowfullscreen', True)
        elif self.allowfullscreen is not None and not self.allowfullscreen:
            attr.setdefault('allowfullscreen', False)
        if self.allowpaymentrequest is not None and self.allowpaymentrequest:
            attr.setdefault('allowpaymentrequest', True)
        elif self.allowpaymentrequest is not None and not self.allowpaymentrequest:
            attr.setdefault('allowpaymentrequest', False)
        if self.height is not None: attr.setdefault('height', self.height)
        if self.width is not None: attr.setdefault('width', self.width)
        if self.loading is not None and self.loading in IFrame.Loading.__members__.values(): attr.setdefault('loading',
                                                                                                             IFrame.Loading[
                                                                                                                 self.loading.name])
        if self.referrerpolicy is not None and self.referrerpolicy in IFrame.Referrerpolicy.__members__.values(): attr.setdefault(
            'referrerpolicy', IFrame.Referrerpolicy[self.referrerpolicy.name])
        if self.sandbox is not None and self.sandbox in IFrame.Sandbox.__members__.values(): attr.setdefault('sandbox',
                                                                                                             IFrame.Sandbox[
                                                                                                                 self.sandbox.name])
        if self.src is not None: attr.setdefault('src', self.src)
        if self.srcdoc is not None: attr.setdefault('srcdoc', self.srcdoc)

        super().__init__('iframe', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
