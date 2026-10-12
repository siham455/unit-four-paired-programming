from lib.music import *
import pytest

def test_add_track():
    music = Music()
    music.add_track("Track 1")
    assert music.tracks == ["Track 1"]

def test_multiple_tracks():
    music = Music()
    music.add_track("Track 1")
    music.add_track("Track 2")
    music.add_track("Track 3")
    assert music.list_tracks() == ["Track 1", "Track 2", "Track 3"]

def test_empty_list():
    music = Music()
    with pytest.raises(Exception) as e:
        music.list_tracks()
    error_message = str(e.value)
    assert error_message == "No tracks in the library"

def test_empty_track():
    music = Music()
    with pytest.raises(Exception) as e:
        music.add_track("")
    error_message = str(e.value)
    assert error_message == "Please add a track" 