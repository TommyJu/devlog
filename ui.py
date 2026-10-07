import curses
from ascii_art import TIMER_ART

def initialize_ui(stdscr):
    curses.start_color()
    stdscr.nodelay(True)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.bkgd(" ", curses.color_pair(3))
    
    
def render(app_state, stdscr):
    stdscr.erase()
    
    display_art(stdscr, 2, 5)
    display_controls(stdscr)
    
    start_datetime = app_state.get_start_datetime()
    display_start_datetime(stdscr, start_datetime)
    
    if app_state.paused:
        display_program_status(stdscr, False)
        elapsed_time = app_state.get_elapsed_time()
        display_elapsed_time(stdscr, elapsed_time, False)
    else:
        display_program_status(stdscr, True)
        elapsed_time = app_state.get_elapsed_time()
        display_elapsed_time(stdscr, elapsed_time, True)
    

# Helper Functions ---------------------
def display_controls(stdscr):
    height, width = stdscr.getmaxyx()
    controls = "[Q] Quit  [SPACE] Pause/Resume"
    stdscr.addstr(height - 2, 1, controls[:width - 1])
    
def display_program_status(stdscr, is_running):
    if is_running:
        stdscr.addstr(2, 1, "Program Status: RUNNING", curses.color_pair(1))
    else:
        stdscr.addstr(2, 1, "Program Status: PAUSED", curses.color_pair(2))
    
    
def display_elapsed_time(stdscr, message, is_running):
    if is_running:  
        stdscr.addstr(3, 1, f"Elapsed Time: {message}", curses.color_pair(3) | curses.A_ITALIC)
    else:
        stdscr.addstr(3, 1, f"Elapsed Time: {message}", curses.color_pair(3) | curses.A_ITALIC | curses.A_BLINK)
        
def display_start_datetime(stdscr, message):
    stdscr.addstr(1, 1, f"Session Start: {message}", curses.color_pair(3) | curses.A_DIM)
    
    
def display_art(stdscr, y, x):

    height, width = stdscr.getmaxyx()

    controls_y = height - 2

    for row, line in enumerate(TIMER_ART.splitlines()):

        current_y = y + row

        # Don't draw into the controls area
        if current_y >= controls_y:
            break

        # Clip the right side if necessary
        available_width = width - x - 1

        if available_width <= 0:
            break

        stdscr.addstr(
            current_y,
            x,
            line[:available_width],
            curses.color_pair(4)
        )
    
