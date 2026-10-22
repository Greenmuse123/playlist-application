import unittest

from app import format_duration, parse_duration


class AppHelperTests(unittest.TestCase):
    def test_parse_duration_converts_minutes_and_seconds(self):
        self.assertEqual(parse_duration("3:45"), 225)

    def test_parse_duration_rejects_out_of_range_seconds(self):
        with self.assertRaisesRegex(ValueError, "M:SS"):
            parse_duration("3:75")

    def test_format_duration_pads_seconds(self):
        self.assertEqual(format_duration(245), "4:05")


if __name__ == "__main__":
    unittest.main()

