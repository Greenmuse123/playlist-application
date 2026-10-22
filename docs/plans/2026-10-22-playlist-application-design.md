# Playlist Application Design

The project is a small Python command-line application for managing a music playlist. A `Song` value stores a title, artist, and duration in seconds. A `Playlist` object owns the ordered song collection and provides the application behavior. The first version supports adding songs, removing songs by title, listing songs, and calculating the playlist's total duration. Keeping the model independent from terminal input makes every behavior straightforward to test.

The command-line entry point presents a numbered menu and translates user input into calls on `Playlist`. Invalid menu choices and malformed durations are reported without terminating the program. The application uses only Python's standard library, so setup stays appropriate for a small classroom collaboration exercise.

Development demonstrates the required Git workflow. The tested initial application is committed and pushed from `master`. Two branches then start from that same initial commit. `partner-one/song-search` adds case-insensitive song search, while `partner-two/playlist-statistics` adds a song-count function. Because the changes affect separate methods and tests, they are independent and can be merged back with explicit merge commits. All commits use the repository owner's configured Git identity and contain no AI co-author trailer.

