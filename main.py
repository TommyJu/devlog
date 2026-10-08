import time
import curses
from input_handling import handle_input
from ui.render import initialize_ui, render
from AppState import AppState
from ScreenState import ScreenState

def main(stdscr):
    # Initialization
    initialize_ui(stdscr)
    app_state = AppState()
    try:
        while app_state.running:

            handle_input(
                stdscr,
                app_state
            )

            render(
                stdscr,
                app_state,
            )

            stdscr.refresh()
            
            # Speed up main loop when writing notes for a responsive input UX
            if app_state.screen == ScreenState.SESSION_NOTES:
                time.sleep(0.03)
            else:
                time.sleep(0.3)
        
        # TODO: Handle session save
    except KeyboardInterrupt:
        pass
    
curses.wrapper(main)