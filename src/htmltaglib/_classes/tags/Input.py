from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Input(Element):
    """Represents an HTML Input Element;
    Defines an input control.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword accept: List of Input.Accept's and Str; Specifies a filter for what file types the user can pick from the file input dialog box (only for type="file"). (default: None)
    :keyword alt: Str; Specifies an alternate text for images (only for type="image"). (default: None)
    :keyword autocomplete: Bool; Specifies whether an input element should have autocomplete enabled. (default: None)
    :keyword autofocus: Bool; Specifies that an input element should automatically get focus when the page loads. (default: False)
    :keyword checked: Bool; Specifies that an input element should be pre-selected when the page loads (for type="checkbox" or type="radio"). (default: False)
    :keyword dirname: Str; Specifies that the text direction will be submitted. (default: None)
    :keyword disabled: Bool; Specifies that an input element should be disabled. (default: False)
    :keyword form: Str; Specifies the form the input element belongs to. (default: None)
    :keyword formaction: Str; Specifies the URL of the file that will process the input control when the form is submitted (for type="submit" and type="image"). (default: None)
    :keyword formenctype: Form.EncType; Specifies how the form-data should be encoded when submitting it to the server (for type="submit" and type="image"). (default: None)
    :keyword formmethod: Form.Method; Defines the HTTP method for sending data to the action URL (for type="submit" and type="image"). (default: None)
    :keyword formnovalidate: Bool; Defines that form elements should not be validated when submitted. (default: False)
    :keyword formtarget: Form.Target or Str; Specifies where to display the response that is received after submitting the form (for type="submit" and type="image"). (default: None)
    :keyword height: Float; Specifies the height of an input element (only for type="image"). (default: None)
    :keyword width: Float; Specifies the width of an input element (only for type="image"). (default: None)
    :keyword list: Str; Refers to a <datalist> element that contains pre-defined options for an input element. (default: None)
    :keyword max: Str or Int; Specifies the maximum value for an input element. (default: None)
    :keyword maxlength: Int; Specifies the maximum number of characters allowed in an input element. (default: None)
    :keyword min: Str or Int; Specifies a minimum value for an input element. (default: None)
    :keyword minlength: Int; Specifies the minimum number of characters required in an input element. (default: None)
    :keyword multiple: Bool; Specifies that a user can enter more than one value in an input element. (default: False)
    :keyword name: Str; Specifies the name of an input element. (default: None)
    :keyword pattern: Str; Specifies a regular expression that an input element's value is checked against. (default: None)
    :keyword placeholder: Str; Specifies a short hint that describes the expected value of an input element. (default: None)
    :keyword readonly: Bool; Specifies that an input field is read-only. (default: False)
    :keyword required: Bool; Specifies that an input field must be filled out before submitting the form. (default: False)
    :keyword size: Int; Specifies the width, in characters, of an input element. (default: None)
    :keyword src: Str; Specifies the URL of the image to use as a submit button (only for type="image"). (default: None)
    :keyword step: Str; Specifies the interval between legal numbers in an input field. (default: None)
    :keyword value: Str; Specifies the value of an input element. (default: None) """

    class Type(CustomEnum):
        BUTTON = 'button'
        CHECKBOX = 'checkbox'
        COLOR = 'color'
        DATE = 'date'
        DATETIME = 'datetime-local'
        EMAIL = 'email'
        FILE = 'file'
        HIDDEN = 'hidden'
        IMAGE = 'image'
        MONTH = 'month'
        NUMBER = 'number'
        PASSWORD = 'password'
        RADIO = 'radio'
        RANGE = 'range'
        RESET = 'reset'
        SEARCH = 'search'
        SUBMIT = 'submit'
        TEL = 'tel'
        TEXT = 'text'
        TIME = 'time'
        URL = 'url'
        WEEK = 'week'

    class Accept(CustomEnum):
        FILE_EXTENSION = 'file_extension'
        AUDIO = 'audio/*'
        VIDEO = 'video/*'
        IMAGE = 'image/*'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.HTMLtype: Input.Type = kwargs.get('HTMLtype', Input.Type.TEXT)
        if self.HTMLtype is None: self.HTMLtype = Input.Type.TEXT

        self.accept: list[Input.Accept, str] = kwargs.get('accept',
                                                          None)  # Specifies a filter for what file types the user can pick from the file input dialog box (only for type="file")
        self.alt: str = kwargs.get('alt', None)  # Specifies an alternate text for images (only for type="image")
        self.autocomplete: bool = kwargs.get('autocomplete',
                                             None)  # Specifies whether an input element should have autocomplete enabled
        self.autofocus: bool = kwargs.get('autofocus',
                                          False)  # Specifies that an input element should automatically get focus when the page loads
        self.checked: bool = kwargs.get('checked',
                                        False)  # Specifies that an input element should be pre-selected when the page loads (for type="checkbox" or type="radio")
        self.dirname: str = kwargs.get('dirname', None)  # Specifies that the text direction will be submitted
        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that an input element should be disabled
        self.form: str = kwargs.get('form', None)  # Specifies the form the input element belongs to
        self.formaction: str = kwargs.get('formaction',
                                          None)  # Specifies the URL of the file that will process the input control when the form is submitted (for type="submit" and type="image")
        self.formenctype: Form.EncType = kwargs.get('formenctype',
                                                    None)  # Specifies how the form-data should be encoded when submitting it to the server (for type="submit" and type="image")
        self.formmethod: Form.Method = kwargs.get('formmethod',
                                                  None)  # Defines the HTTP method for sending data to the action URL (for type="submit" and type="image")
        self.formnovalidate: bool = kwargs.get('formnovalidate',
                                               False)  # Defines that form elements should not be validated when submitted
        self.formtarget: [Form.Target, str] = kwargs.get('formtarget',
                                                         None)  # Specifies where to display the response that is received after submitting the form (for type="submit" and type="image")
        self.height: float = kwargs.get('height',
                                        None)  # Specifies the height of an input element (only for type="image")
        self.width: float = kwargs.get('width',
                                       None)  # Specifies the width of an input element (only for type="image")
        self.list: str = kwargs.get('list',
                                    None)  # Refers to a datalist element that contains pre-defined options for an input element
        self.max: [str, int] = kwargs.get('max', None)  # Specifies the maximum value for an input element
        self.maxlength: int = kwargs.get('maxlength',
                                         None)  # Specifies the maximum number of characters allowed in an input element
        self.min: [str, int] = kwargs.get('min', None)  # Specifies a minimum value for an input element
        self.minlength: int = kwargs.get('minlength',
                                         None)  # Specifies the minimum number of characters required in an input element
        self.multiple: bool = kwargs.get('multiple',
                                         False)  # Specifies that a user can enter more than one value in an input element
        self.name: str = kwargs.get('name', None)  # Specifies the name of an input element
        self.pattern: str = kwargs.get('pattern',
                                       None)  # Specifies a regular expression that an input element's value is checked against
        self.placeholder: str = kwargs.get('placeholder',
                                           None)  # Specifies a short hint that describes the expected value of an input element
        self.readonly: bool = kwargs.get('readonly', False)  # Specifies that an input field is read-only
        self.required: bool = kwargs.get('required',
                                         False)  # Specifies that an input field must be filled out before submitting the form
        self.size: int = kwargs.get('size', None)  # Specifies the width, in characters, of an input element
        self.src: str = kwargs.get('src',
                                   None)  # Specifies the URL of the image to use as a submit button (only for type="image")
        self.step: str = kwargs.get('step', None)  # Specifies the interval between legal numbers in an input field
        self.value: str = kwargs.get('value', None)  # Specifies the value of an input element

        attr.setdefault('type', self.HTMLtype.value)

        if self.HTMLtype == Input.Type.CHECKBOX or self.HTMLtype == Input.Type.RADIO:
            if self.checked: attr.setdefault('checked', None)
        elif self.HTMLtype == Input.Type.FILE:
            if self.accept is not None and len(self.accept) > 0:
                if len(self.accept) == 1:
                    if self.accept[0] in Input.Accept.__members__.values():
                        attr.setdefault('accept', Input.Accept[self.accept[0].name])
                    else:
                        attr.setdefault('accept', self.accept[0])
                elif len(self.accept) > 1:
                    for _ in self.accept: _ = str(_)
                    self.accept: list[str]
                    attr.setdefault('accept', ','.join(self.accept))
        elif self.HTMLtype == Input.Type.IMAGE:
            if self.alt is not None: attr.setdefault('alt', self.alt)
            if self.formaction is not None: attr.setdefault('formaction', self.formaction)
            if self.formenctype is not None and self.formenctype in Form.EncType.__members__.values(): attr.setdefault(
                'formenctype', Form.EncType[self.formenctype.name])
            if self.formmethod is not None and self.formmethod in Form.Method.__members__.values(): attr.setdefault(
                'formmethod', Form.Method[self.formmethod.name])
            if self.formtarget is not None and self.formtarget in Form.Target.__members__.values(): attr.setdefault(
                'formtarget', Form.Target[self.formtarget.name])
            if self.height is not None: attr.setdefault('height', self.height)
            if self.width is not None: attr.setdefault('width', self.width)
            if self.src is not None: attr.setdefault('src', self.src)
        elif self.HTMLtype == Input.Type.SUBMIT:
            if self.formaction is not None: attr.setdefault('formaction', self.formaction)
            if self.formenctype is not None and self.formenctype in Form.EncType.__members__.values(): attr.setdefault(
                'formenctype', Form.EncType[self.formenctype.name])
            if self.formmethod is not None and self.formmethod in Form.Method.__members__.values(): attr.setdefault(
                'formmethod', Form.Method[self.formmethod.name])
            if self.formtarget is not None and self.formtarget in Form.Target.__members__.values(): attr.setdefault(
                'formtarget', Form.Target[self.formtarget.name])

        if self.autocomplete is not None: attr.setdefault('autocomplete',
                                                          'on') if self.autocomplete else attr.setdefault(
            'autocomplete', 'off')
        if self.autofocus: attr.setdefault('autofocus', None)
        if self.dirname is not None:
            if self.dirname[-4:-1] != '.dir': self.dirname += '.dir'
            attr.setdefault('dirname', self.dirname)
        if self.disabled: attr.setdefault('disabled', None)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.formnovalidate: attr.setdefault('formnovalidate', None)
        if self.list is not None: attr.setdefault('list', self.list)
        if self.max is not None: attr.setdefault('max', str(self.max))
        if self.maxlength is not None: attr.setdefault('maxlength', str(self.max))
        if self.min is not None: attr.setdefault('min', str(self.min))
        if self.minlength is not None: attr.setdefault('minlength', str(self.max))
        if self.multiple: attr.setdefault('multiple', None)
        if self.name is not None: attr.setdefault('name', self.name)
        if self.pattern is not None: attr.setdefault('pattern', self.pattern)
        if self.placeholder is not None: attr.setdefault('placeholder', self.placeholder)
        if self.readonly: attr.setdefault('readonly', None)
        if self.required: attr.setdefault('required', None)
        if self.size is not None: attr.setdefault('size', self.size)
        if self.step is not None: attr.setdefault('step', str(self.step))
        if self.value is not None: attr.setdefault('value', str(self.value))

        super().__init__('input', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
