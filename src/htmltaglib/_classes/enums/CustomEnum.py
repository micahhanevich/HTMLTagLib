from enum import Enum


class CustomEnum(Enum):
    def __str__(self):
        return '{0}'.format(self.value)
