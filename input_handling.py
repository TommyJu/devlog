from time import time
from ScreenState import ScreenState
import curses
from save_session import save_session

def handle_input(stdscr, app_state):
    key = stdscr.getch()
    
    if app_state.screen == ScreenState.TIMER:
        handle_timer_screen_input(key, app_state)
    
    elif app_state.screen == ScreenState.SAVE_SESSION:
        handle_save_session_input(key, app_state)
            
    elif app_state.screen == ScreenState.SESSION_NOTES:
        handle_session_notes_input(key, app_state)

# Helper Functions ---------------    
def handle_timer_screen_input(key, app_state):
    # Pause/resume
    if key == ord(" "):
        app_state.timer.toggle_pause()

    # End Session
    elif key == ord("q"):
        app_state.timer.stop_timer()
        app_state.screen = ScreenState.SAVE_SESSION
        
        
def handle_save_session_input(key, app_state):
    if key in (ord("y"), ord("Y")):
        app_state.screen = ScreenState.SESSION_NOTES
    
    if key in (ord("n"), ord("N")):
        app_state.running = False
        
def handle_session_notes_input(key, app_state):
    if key in (curses.KEY_ENTER, 10):
        save_session(app_state)
        app_state.running = False

    elif key in (curses.KEY_BACKSPACE, 127, 8):
        app_state.session_notes = app_state.session_notes[:-1]

    elif 32 <= key <= 126:
        app_state.session_notes += chr(key)