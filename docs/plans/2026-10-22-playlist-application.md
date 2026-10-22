# Playlist Application Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build and publish a tested Python playlist application while demonstrating two independent feature branches merged into `master`.

**Architecture:** `playlist.py` contains the `Song` and `Playlist` domain model. `app.py` provides a thin interactive command-line interface. Standard-library `unittest` tests behavior without external dependencies.

**Tech Stack:** Python 3, `dataclasses`, `unittest`, Git

---

### Task 1: Initial playlist model

**Files:**
- Create: `tests/test_playlist.py`
- Create: `playlist.py`

1. Write failing tests for adding, removing, listing, and totaling songs.
2. Run `python -m unittest discover -s tests -v` and confirm the model import fails.
3. Implement the minimal `Song` and `Playlist` model.
4. Run the test suite and confirm it passes.

### Task 2: Command-line interface and documentation

**Files:**
- Create: `tests/test_app.py`
- Create: `app.py`
- Create: `README.md`

1. Write failing tests for duration parsing and menu behavior.
2. Run the focused tests and confirm they fail because the functions do not exist.
3. Implement the CLI helpers and menu loop.
4. Run all tests.
5. Document the project, commands, features, and collaboration workflow.
6. Commit the initial project on `master` and push it.

### Task 3: Partner one song search

**Files:**
- Modify: `tests/test_playlist.py`
- Modify: `playlist.py`

1. Create `partner-one/song-search` from the initial-project commit.
2. Write and run a failing case-insensitive search test.
3. Implement `search_songs` and run all tests.
4. Commit and push the branch.

### Task 4: Partner two playlist statistics

**Files:**
- Modify: `tests/test_playlist.py`
- Modify: `playlist.py`

1. Create `partner-two/playlist-statistics` from the initial-project commit.
2. Write and run a failing song-count test.
3. Implement `song_count` and run all tests.
4. Commit and push the branch.

### Task 5: Merge and verify

1. Merge both feature branches into `master` using `--no-ff`.
2. Run `python -m unittest discover -s tests -v`.
3. Inspect the graph with `git log --graph --decorate --oneline --all`.
4. Inspect commit bodies and verify there are no `Co-authored-by` trailers.
5. Push `master` and both feature branches.

