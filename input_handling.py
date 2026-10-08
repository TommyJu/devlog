from time import time
from ScreenState import ScreenState

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
    timer = app_state.timer
    
    if key == ord(" "):
        if not timer.paused:
            # Save the time accumulated before pausing
            timer.elapsed_accumulated += time() - timer.start
            timer.paused = True

        else:
            # Start a new timing period
            timer.start = time()
            timer.paused = False

    elif key == ord("q"):
        app_state.screen = ScreenState.SAVE_SESSION
        
def handle_save_session_input(key, app_state):
    if key in (ord("y"), ord("Y")):
        app_state.screen = ScreenState.SESSION_NOTES
    
    if key in (ord("n"), ord("N")):
        app_state.running = False
        
def handle_session_notes_input(key, app_state):
    ...