from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Meter(Element):
    """Represents an HTML Meter Element;
    Defines a scalar measurement within a known range (a gauge).

    :param value: Float; Required. Specifies the current value of the gauge

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword form: Str; Specifies which form the meter element belongs to. (default: None)
    :keyword high: Float; Specifies the range that is considered to be a high value. (default: None)
    :keyword low: Float; Specifies the range that is considered to be a low value. (default: None)
    :keyword max: Float; Specifies the maximum value of the range. (default: None)
    :keyword min: Float; Specifies the minimum value of the range. Default value is 0. (default: None)
    :keyword optimum: Float; Specifies what value is the optimal value for the gauge. (default: None) """

    def __init__(self, value: float, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.form: str = kwargs.get('form', None)  # Specifies which form the <meter> element belongs to
        self.high: float = kwargs.get('high', None)  # Specifies the range that is considered to be a high value
        self.low: float = kwargs.get('low', None)  # Specifies the range that is considered to be a low value
        self.max: float = kwargs.get('max', None)  # Specifies the maximum value of the range
        self.min: float = kwargs.get('min', None)  # Specifies the minimum value of the range. Default value is 0
        self.optimum: float = kwargs.get('optimum', None)  # Specifies what value is the optimal value for the gauge
        self.value: float = value  # Required. Specifies the current value of the gauge

        attr.setdefault('value', self.value)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.high is not None: attr.setdefault('high', self.high)
        if self.low is not None: attr.setdefault('low', self.low)
        if self.max is not None: attr.setdefault('max', self.max)
        if self.min is not None: attr.setdefault('min', self.min)
        if self.optimum is not None: attr.setdefault('optimum', self.optimum)

        super().__init__('meter', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
