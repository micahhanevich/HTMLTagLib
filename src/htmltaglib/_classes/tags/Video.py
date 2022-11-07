from ..enums.CustomEnum import CustomEnum
from ..Element import Element


class Video(Element):
    """Represents an HTML Video Element;
    Defines embedded video content.

    :keyword attr: Attributes Dictionary that places items as an attribute in an Element. (default: {})
    :keyword html: Str to override object's generated HTML value. Does not update the rest of the object to reflect HTML str. (default: None)

    :keyword autoplay: Bool; Specifies that the video will start playing as soon as it is ready. (default: False)
    :keyword controls: Bool; Specifies that video controls should be displayed (such as a play/pause button etc). (default: False)
    :keyword height: Float; Sets the height of the video player. (default: None)
    :keyword width: Float; Sets the width of the video player. (default: None)
    :keyword loop: Bool; Specifies that the video will start over again, every time it is finished. (default: False)
    :keyword muted: Bool; Specifies that the audio output of the video should be muted. (default: False)
    :keyword poster: Str; Specifies an image to be shown while the video is downloading, or until the user hits the play button. (default: None)
    :keyword preload: Video.Preload; Specifies if and how the author thinks the video should be loaded when the page loads. (default: None)
    :keyword src: Str; Specifies the URL of the video file. (default: None) """

    class Preload(CustomEnum):
        AUTO = 'auto'
        METADATA = 'metadata'
        NONE = 'none'

    def __init__(self, items: list = None, **kwargs):
        attr: dict = kwargs.get('attr', {})
        html: str = kwargs.get('html', None)

        self.autoplay: bool = kwargs.get('autoplay',
                                         False)  # Specifies that the video will start playing as soon as it is ready
        self.controls: bool = kwargs.get('controls',
                                         False)  # Specifies that video controls should be displayed (such as a play/pause button etc).
        self.height: float = kwargs.get('height', None)  # Sets the height of the video player
        self.width: float = kwargs.get('width', None)  # Sets the width of the video player
        self.loop: bool = kwargs.get('loop',
                                     False)  # Specifies that the video will start over again, every time it is finished
        self.muted: bool = kwargs.get('muted', False)  # Specifies that the audio output of the video should be muted
        self.poster: str = kwargs.get('poster',
                                      None)  # Specifies an image to be shown while the video is downloading, or until the user hits the play button
        self.preload: Video.Preload = kwargs.get('preload',
                                                 None)  # Specifies if and how the author thinks the video should be loaded when the page loads
        self.src: str = kwargs.get('src', None)  # Specifies the URL of the video file

        if self.autoplay: attr.setdefault('autoplay', None)
        if self.controls: attr.setdefault('controls', None)
        if self.height is not None: attr.setdefault('height', self.height)
        if self.width is not None: attr.setdefault('width', self.width)
        if self.loop: attr.setdefault('loop', None)
        if self.muted: attr.setdefault('muted', None)
        if self.poster is not None: attr.setdefault('poster', self.poster)
        if self.preload is not None and self.preload in Video.Preload.__members__.values(): attr.setdefault(
            Video.Preload[self.preload.name])
        if self.src is not None: attr.setdefault('src', self.src)

        super().__init__('video', attr=attr, html=html, end_tag=True)
        if items is not None: self.set_items(items)
