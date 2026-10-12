# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Music:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   None

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   A list of the tracks
        # Side-effects:
        #   None
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a track
#adds the track to the self object
"""
music = Music()
music.add_track("Track 1")
music.tracks == ["Track 1"]

"""
Given multiple tracks
#returns a list containing all the tracks 
"""
music = Music()
music.add_track("Track 1")
music.add_track("Track 2")
music.add_track("Track 3")
music.list_tracks() == ["Track 1", "Track 2", "Track 3"]

"""
Given an empty list
#raise an exception
"""
music = Music()
music.list_tracks() => # raise an exception 'No tracks in the library'

"""
Given an empty track
#raise an exception
"""
music = Music()
music.add_track('') => # raise an exception 'Please add a track'


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
