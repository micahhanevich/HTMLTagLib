from ..enums.CustomEnum import CustomEnum
from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Track(Element):
    """Represents an HTML Track Element;
    Defines text tracks for media elements (<video> and <audio>).

    :param src: Str; Required. Specifies the URL of the track file.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword default: Bool; Specifies that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate. (default: False)
    :keyword kind: Track.Kind; Specifies the kind of text track. (default: None)
    :keyword label: Str; Specifies the title of the text track. (default: None)
    :keyword srclang: Str; Specifies the language of the track text data (required if kind="subtitles"). (default: None) """

    class Kind(CustomEnum):
        CAPTIONS = 'captions'
        CHAPTERS = 'chapters'
        DESCRIPTIONS = 'descriptions'
        METADATA = 'metadata'
        SUBTITLES = 'subtitles'

    def __init__(self, src: str, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.default: bool = kwargs.get('default',
                                        False)  # Specifies that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate
        self.kind: Track.Kind = kwargs.get('kind', None)  # Specifies the kind of text track
        self.label: str = kwargs.get('label', None)  # Specifies the title of the text track
        self.src: str = src  # Required. Specifies the URL of the track file
        self.srclang: str = kwargs.get('srclang',
                                       None)  # Specifies the language of the track text data (required if kind="subtitles")

        if self.default: attr.setdefault('default', None)
        if self.kind is not None and self.kind in Track.Kind.__members__.values(): attr.setdefault('kind', Track.Kind[
            self.kind.name])
        if self.label is not None: attr.setdefault('label', self.label)
        if self.kind == Track.Kind.SUBTITLES:
            attr.setdefault('src', self.srclang)
        elif self.srclang is not None:
            attr.setdefault('src', self.srclang)

        super().__init__('track', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
