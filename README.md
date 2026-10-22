# Playlist Application

Playlist Application is a small Python command-line program for creating and managing a music playlist. It was built as a collaborative Git exercise that demonstrates independent feature branches and merges back into the `master` branch.

## Features

- Create a named playlist.
- Add songs with a title, artist, and duration.
- Remove a song by title without case-sensitive matching.
- Display songs in playlist order.
- Show the playlist's total duration.

## Requirements

- Python 3.10 or newer

The project uses only the Python standard library, so no packages need to be installed.

## Run the application

From the project directory:

```bash
python app.py
```

Enter song durations using `minutes:seconds`, such as `3:45`.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
playlist-application/
|-- app.py              # Command-line menu and duration helpers
|-- playlist.py         # Song and Playlist classes
|-- tests/              # Automated unit tests
|-- docs/plans/         # Design and implementation notes
`-- README.md
```

## Collaboration workflow

The initial project is committed on `master`. Each partner creates a branch from that shared starting point, implements and tests an independent change, and then merges the branch back into `master`.

```bash
git switch -c partner-name/feature-name
# Make and test the change.
git add .
git commit -m "feat: describe the change"
git switch master
git merge --no-ff partner-name/feature-name
git push origin master
```

This repository demonstrates the workflow with two independent branches:

- `partner-one/song-search` adds case-insensitive song search.
- `partner-two/playlist-statistics` adds a song-count function.

