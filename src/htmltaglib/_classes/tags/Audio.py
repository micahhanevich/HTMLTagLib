from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Audio(Element):
    """Represents an HTML Audio element;
    Defines embedded sound content.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword autoplay: Bool; Specifies that the audio will start playing as soon as it is ready. (default: False)
    :keyword controls: Bool; Specifies that audio controls should be displayed (such as a play/pause button etc). (default: False)
    :keyword loop: Bool; Specifies that the audio will start over again, every time it is finished. (default: False)
    :keyword muted: Bool; Specifies that the audio output should be muted. (default: False)
    :keyword preload: Audio.Preload; Specifies if and how the author thinks the audio should be loaded when the page loads. (default: None) """

    class Preload(CustomEnum):
        AUTO = 'auto'
        METADATA = 'metadata'
        NONE = 'none'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.autoplay: bool = kwargs.get('autoplay',
                                         False)  # Specifies that the audio will start playing as soon as it is ready
        self.controls: bool = kwargs.get('controls',
                                         False)  # Specifies that audio controls should be displayed (such as a play/pause button etc)
        self.loop: bool = kwargs.get('loop',
                                     False)  # Specifies that the audio will start over again, every time it is finished
        self.muted: bool = kwargs.get('muted', False)  # Specifies that the audio output should be muted
        self.preload: Audio.Preload = kwargs.get('preload',
                                                 None)  # Specifies if and how the author thinks the audio should be loaded when the page loads

        if self.autoplay: attr.setdefault('autoplay', None)
        if self.controls: attr.setdefault('controls', None)
        if self.loop: attr.setdefault('loop', None)
        if self.muted: attr.setdefault('muted', None)
        if self.preload is not None and self.preload in Audio.Preload.__members__.values(): attr.setdefault('preload',
                                                                                                            Audio.Preload[
                                                                                                                self.preload.name])

        super().__init__('audio', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
