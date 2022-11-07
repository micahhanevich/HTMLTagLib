from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class TextArea(Element):
    """Represents an HTML TextArea Element;
    Defines a multiline input control (text area).

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword autofocus: Bool; Specifies that a text area should automatically get focus when the page loads. (default: False)
    :keyword cols: Int; Specifies the visible width of a text area. (default: None)
    :keyword rows: Int; Specifies the visible number of lines in a text area. (default: None)
    :keyword dirname: Str; Specifies that the text direction of the textarea will be submitted. (default: None)
    :keyword disabled: Bool; Specifies that a text area should be disabled. (default: False)
    :keyword form: Str; Specifies which form the text area belongs to. (default: None)
    :keyword maxlength: Int; Specifies the maximum number of characters allowed in the text area. (default: None)
    :keyword name: Str; Specifies a name for a text area. (default: None)
    :keyword placeholder: Str; Specifies a short hint that describes the expected value of a text area. (default: None)
    :keyword readonly: Bool; Specifies that a text area should be read-only. (default: False)
    :keyword required: Bool; Specifies that a text area is required/must be filled out. (default: False)
    :keyword wrap: TextArea.Wrap; Specifies how the text in a text area is to be wrapped when submitted in a form. (default: None) """

    class Wrap(CustomEnum):
        HARD = 'hard'
        SOFT = 'soft'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.autofocus: bool = kwargs.get('autofocus',
                                          False)  # Specifies that a text area should automatically get focus when the page loads
        self.cols: int = kwargs.get('cols', None)  # Specifies the visible width of a text area
        self.rows: int = kwargs.get('rows', None)  # Specifies the visible number of lines in a text area
        self.dirname: str = kwargs.get('dirname',
                                       None)  # Specifies that the text direction of the textarea will be submitted
        self.disabled: bool = kwargs.get('disabled', False)  # Specifies that a text area should be disabled
        self.form: str = kwargs.get('form', None)  # Specifies which form the text area belongs to
        self.maxlength: int = kwargs.get('maxlength',
                                         None)  # Specifies the maximum number of characters allowed in the text area
        self.name: str = kwargs.get('name', None)  # Specifies a name for a text area
        self.placeholder: str = kwargs.get('placeholder',
                                           None)  # Specifies a short hint that describes the expected value of a text area
        self.readonly: bool = kwargs.get('readonly', False)  # Specifies that a text area should be read-only
        self.required: bool = kwargs.get('required', False)  # Specifies that a text area is required/must be filled out
        self.wrap: TextArea.Wrap = kwargs.get('wrap',
                                              None)  # Specifies how the text in a text area is to be wrapped when submitted in a form

        if self.autofocus: attr.setdefault('autofocus', None)
        if self.cols is not None: attr.setdefault('cols', self.cols)
        if self.rows is not None: attr.setdefault('rows', self.rows)
        if self.dirname is not None: attr.setdefault('dirname', self.dirname if self.dirname[
                                                                                -4:-1] == '.dir' else self.dirname + '.dir')
        if self.disabled: attr.setdefault('disabled', None)
        if self.form is not None: attr.setdefault('form', self.form)
        if self.maxlength is not None: attr.setdefault('maxlength', self.maxlength)
        if self.name is not None: attr.setdefault('name', self.name)
        if self.placeholder is not None: attr.setdefault('placeholder', self.placeholder)
        if self.readonly: attr.setdefault('readonly', None)
        if self.required: attr.setdefault('required', None)
        if self.wrap is not None and self.wrap in TextArea.Wrap.__members__.values(): attr.setdefault('wrap',
                                                                                                      TextArea.Wrap[
                                                                                                          self.wrap.name])

        super().__init__('textarea', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
