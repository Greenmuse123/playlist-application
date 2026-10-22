"""Interactive command-line interface for the playlist application."""

from playlist import Playlist, Song


def parse_duration(value: str) -> int:
    """Convert an M:SS duration to seconds."""
    try:
        minutes_text, seconds_text = value.strip().split(":", maxsplit=1)
        minutes = int(minutes_text)
        seconds = int(seconds_text)
    except (TypeError, ValueError) as error:
        raise ValueError("Duration must use M:SS format") from error

    if minutes < 0 or seconds < 0 or seconds > 59:
        raise ValueError("Duration must use M:SS format")
    return minutes * 60 + seconds


def format_duration(total_seconds: int) -> str:
    """Format a duration in seconds as M:SS."""
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"


def display_playlist(playlist: Playlist) -> None:
    """Print all songs and the total playlist duration."""
    songs = playlist.list_songs()
    if not songs:
        print("The playlist is empty.")
        return

    for number, song in enumerate(songs, start=1):
        duration = format_duration(song.duration_seconds)
        print(f"{number}. {song.title} - {song.artist} ({duration})")
    print(f"Total duration: {format_duration(playlist.total_duration())}")


def main() -> None:
    """Run the playlist menu until the user chooses to exit."""
    playlist = Playlist(input("Playlist name: ").strip() or "My Playlist")

    while True:
        print("\n1. Add song")
        print("2. Remove song")
        print("3. View playlist")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Song title: ").strip()
            artist = input("Artist: ").strip()
            try:
                duration = parse_duration(input("Duration (M:SS): "))
            except ValueError as error:
                print(error)
                continue
            playlist.add_song(Song(title, artist, duration))
            print(f"Added {title}.")
        elif choice == "2":
            title = input("Title to remove: ").strip()
            removed = playlist.remove_song(title)
            print(f"Removed {removed.title}." if removed else "Song not found.")
        elif choice == "3":
            display_playlist(playlist)
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()

