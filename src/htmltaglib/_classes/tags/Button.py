from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Button(Element):
    """Represents an HTML Button element;
    Defines a clickable button.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword autofocus: Bool; Specifies that a button should automatically get focus when the page loads. (default: False)
    :keyword disabled: Bool; Specifies that a button should be disabled. (default: False)
    :keyword form: Str; Specifies which form the button belongs to. (default: None)
    :keyword formaction: Str; Specifies where to send the form-data when a form is submitted. Only for type="submit". (default: None)
    :keyword formenctype: Form.EncType; Specifies how form-data should be encoded before sending it to a server. Only for type="submit". (default: None)
    :keyword formmethod: Form.Method; Specifies how to send the form-data (which HTTP method to use). Only for type="submit". (default: None)
    :keyword formnovalidate: Bool; Specifies that the form-data should not be validated on submission. Only for type="submit". (default: False)
    :keyword formtarget: Form.Target or Str; Specifies where to display the response after submitting the form. Only for type="submit". (default: None)
    :keyword name: Str; Specifies a name for the button. (default: None)
    :keyword HTMLtype: Button.Type; Specifies the type of button. (default: None)
    :keyword value: Str; Specifies an initial value for the button. (default: None) """

    class Type(CustomEnum):
        BUTTON = 'button'
        RESET = 'reset'
        SUBMIT = 'submit'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.autofocus: bool = kwargs.get('autofocus', False)  # Specifies that a button should automatically get focus when the page loads
        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that a button should be disabled
        self.form: str = kwargs.get('form', None)  # Specifies which form the button belongs to
        self.formaction: str = kwargs.get('formaction', None)  # Specifies where to send the form-data when a form is submitted. Only for type="submit"
        self.formenctype: Form.EncType = kwargs.get('formenctype', None)  # Specifies how form-data should be encoded before sending it to a server. Only for type="submit"
        self.formmethod: Form.Method = kwargs.get('formmethod', None)  # Specifies how to send the form-data (which HTTP method to use). Only for type="submit"
        self.formnovalidate: bool = kwargs.get('formnovalidate', False)  # Specifies that the form-data should not be validated on submission. Only for type="submit"
        self.formtarget: [Form.Target, str] = kwargs.get('formtarget', None)  # Specifies where to display the response after submitting the form. Only for type="submit"
        self.name: str = kwargs.get('name', None)  # Specifies a name for the button
        self.HTMLtype: Button.Type = kwargs.get('HTMLtype', None)  # Specifies the type of button
        self.value: str = kwargs.get('value', None)  # Specifies an initial value for the button

        if self.autofocus: attr.setdefault('autofocus', None)
        if self.disabled: attr.setdefault('disabled', None)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.formaction is not None and self.HTMLtype == Button.Type.SUBMIT: attr.setdefault('formaction', self.formaction)
        if self.formenctype is not None and self.HTMLtype == Button.Type.SUBMIT: attr.setdefault('formenctype', self.formenctype)
        if self.formmethod is not None and self.formmethod in Form.Method and self.HTMLtype == Button.Type.SUBMIT: attr.setdefault('formmethod', self.formmethod)
        if self.formnovalidate is not None and self.HTMLtype == Button.Type.SUBMIT: attr.setdefault('formnovalidate', None)
        if self.formtarget is not None and self.HTMLtype == Button.Type.SUBMIT:
            if self.formtarget in Form.Target.__members__.values():
                attr.setdefault('formtarget', Form.Target[self.formtarget.name])
            else:
                attr.setdefault('formtarget', self.formtarget)
        if self.name is not None: attr.setdefault('name', self.name)
        if self.HTMLtype is not None and self.HTMLtype in Button.Type.__members__.values(): attr.setdefault('type', Button.Type[self.HTMLtype.name])
        elif self.HTMLtype is not None and self.HTMLtype in Button.Type.__members__.keys(): attr.setdefault('type', Button.Type[self.HTMLtype.name])
        if self.value is not None: attr.setdefault('value', self.value)

        super().__init__('button', attr=attr, html=html, end_tag=False)
        if items is not None: self.set_items(items)
