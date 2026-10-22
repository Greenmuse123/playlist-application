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

    def test_search_songs_matches_title_or_artist_without_case_sensitivity(self):
        matching_title = Song("Desert Signal", "Night Radio", 190)
        matching_artist = Song("Open Highway", "The Signals", 210)
        self.playlist.add_song(matching_title)
        self.playlist.add_song(matching_artist)
        self.playlist.add_song(Song("Sunrise", "Morning Band", 180))

        self.assertEqual(
            self.playlist.search_songs("SIGNAL"),
            [matching_title, matching_artist],
        )

    def test_song_rejects_negative_duration(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            Song("Broken", "Unknown", -1)


if __name__ == "__main__":
    unittest.main()

