from entities.const_wheel import SEGMENTS
from entities.const_wheel import SEGMENT_LENGTH
from entities.const_wheel import CIRCLE_DEGREES


class Wheel:

    def __init__(self):
        self.segments = SEGMENTS
        self.position = 0

    def get_segment(self):
        return int(self.position / SEGMENT_LENGTH)

    def spin(self, increments: int):
        self.position = (self.position + increments) % CIRCLE_DEGREES
