from lib.music import *
import pytest

def test_add_track():
    music = Music()
    music.add_track("Track 1")
    assert music.tracks == ["Track 1"]
