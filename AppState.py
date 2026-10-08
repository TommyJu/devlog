from ScreenState import ScreenState
from Timer import Timer

class AppState:
    def __init__(self):
        self.running = True
        self.screen = ScreenState.TIMER
        self.timer = Timer()
        self.session_notes = ""
        