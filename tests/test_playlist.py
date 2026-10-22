import unittest

from playlist import Playlist, Song


class PlaylistTests(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Road Trip")
        self.song = Song("Midnight Drive", "The Signals", 245)

    def test_add_song_keeps_song_in_order(self):
        self.playlist.add_song(self.song)

        self.assertEqual(self.playlist.list_songs(), [self.song])

    def test_remove_song_is_case_insensitive(self):
        self.playlist.add_song(self.song)

        removed = self.playlist.remove_song("MIDNIGHT DRIVE")

        self.assertEqual(removed, self.song)
        self.assertEqual(self.playlist.list_songs(), [])

    def test_remove_song_returns_none_when_title_is_missing(self):
        self.assertIsNone(self.playlist.remove_song("Unknown"))

    def test_total_duration_adds_all_song_durations(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(Song("Sunrise", "The Signals", 180))

        self.assertEqual(self.playlist.total_duration(), 425)

    def test_song_rejects_negative_duration(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            Song("Broken", "Unknown", -1)


if __name__ == "__main__":
    unittest.main()

