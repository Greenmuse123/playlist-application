"""Core playlist data model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Song:
    """A song stored in a playlist."""

    title: str
    artist: str
    duration_seconds: int

    def __post_init__(self) -> None:
        if self.duration_seconds < 0:
            raise ValueError("Song duration must be non-negative")


class Playlist:
    """An ordered collection of songs."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: list[Song] = []

    def add_song(self, song: Song) -> None:
        """Add a song to the end of the playlist."""
        self._songs.append(song)

    def remove_song(self, title: str) -> Song | None:
        """Remove and return the first song matching a title."""
        normalized_title = title.casefold()
        for index, song in enumerate(self._songs):
            if song.title.casefold() == normalized_title:
                return self._songs.pop(index)
        return None

    def list_songs(self) -> list[Song]:
        """Return a copy of the songs in playlist order."""
        return list(self._songs)

    def total_duration(self) -> int:
        """Return the combined song duration in seconds."""
        return sum(song.duration_seconds for song in self._songs)

