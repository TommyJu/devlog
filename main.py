import time
import curses
from input_handling import handle_input
from ui.render import initialize_ui, render
from AppState import AppState

def main(stdscr):
    # Initialization
    initialize_ui(stdscr)
    app_state = AppState()

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

        time.sleep(0.1)
    
    # TODO: Handle session save
curses.wrapper(main)