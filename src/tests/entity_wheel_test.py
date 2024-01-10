from unittest import TestCase

from entities.wheel import Wheel


class TestEntityWheel(TestCase):

    def setUp(self):
        pass

    def test_wheel_has_integer_segment_value(self):
        wheel = Wheel()
        self.assertIsInstance(wheel.segments, int)

    def test_at_start_wheel_position_is_zero(self):
        wheel = Wheel()
        self.assertEqual(wheel.position, 0)

    def test_at_start_wheel_segment_is_zero(self):
        wheel = Wheel()
        segment = wheel.get_segment()

    def test_spinning_wheel_increments_position(self):
        wheel = Wheel()
        wheel.spin(1000)
        self.assertEqual(wheel.get_segment(), 18)

    def test_spinning_wheel_increments_position_multiple_times(self):
        """The wheel has 360 degrees, so 360 increments should bring it back to
        the starting position. This test spins the wheel 1000 increments twice
        and asserts the final segment.
        """
        wheel = Wheel()
        wheel.spin(1000)
        wheel.spin(1000)
        self.assertEqual(wheel.get_segment(), 13)
