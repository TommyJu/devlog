import time
import curses
from AppState import AppState
from input_handling import handle_key_events
from ui import initialize_ui, render


def main(stdscr):
    # Initialization
    initialize_ui(stdscr)
    app_state = AppState()

    while app_state.running:
        # Input handling
        key = stdscr.getch()
        handle_key_events(app_state, key)
        
        # Display logic
        render(app_state, stdscr)
        stdscr.refresh()
        
        # Delay to reduce resource usage
        time.sleep(0.1)

curses.wrapper(main)