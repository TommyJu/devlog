import curses
from ascii_art import TIMER_ART

# Color pair IDs
STATUS_RUNNING = 1
STATUS_PAUSED = 2
TEXT = 3
ART = 4

# Layout
START_DATETIME_Y = 1
STATUS_Y = 2
ELAPSED_TIME_Y = 3
PADDING_X = 1
PADDING_Y = 2

def initialize_ui(stdscr):
    curses.start_color()
    stdscr.nodelay(True)
    curses.init_pair(STATUS_RUNNING, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(STATUS_PAUSED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(TEXT, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(ART, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.bkgd(" ", curses.color_pair(TEXT))
    
    
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
    stdscr.addstr(height - PADDING_Y, PADDING_X, controls[:width - 1])
    
def display_program_status(stdscr, is_running):
    if is_running:
        stdscr.addstr(STATUS_Y, PADDING_X, "Program Status: RUNNING", curses.color_pair(STATUS_RUNNING))
    else:
        stdscr.addstr(STATUS_Y, PADDING_X, "Program Status: PAUSED", curses.color_pair(STATUS_PAUSED))
    
    
def display_elapsed_time(stdscr, message, is_running):
    if is_running:  
        stdscr.addstr(ELAPSED_TIME_Y, PADDING_X, f"Elapsed Time: {message}", curses.color_pair(TEXT) | curses.A_ITALIC)
    else:
        stdscr.addstr(ELAPSED_TIME_Y, PADDING_X, f"Elapsed Time: {message}", curses.color_pair(TEXT) | curses.A_ITALIC | curses.A_BLINK)
        
def display_start_datetime(stdscr, message):
    stdscr.addstr(START_DATETIME_Y, PADDING_X, f"Session Start: {message}", curses.color_pair(TEXT) | curses.A_DIM)
    
    
def display_art(stdscr, y, x):

    height, width = stdscr.getmaxyx()

    controls_y = height - PADDING_Y

    for row, line in enumerate(TIMER_ART.splitlines()):

        current_y = y + row

        # Don't draw into the controls area
        if current_y >= controls_y:
            break

        # Clip the right side if necessary
        available_width = width - x - PADDING_X

        if available_width <= 0:
            break

        stdscr.addstr(
            current_y,
            x,
            line[:available_width],
            curses.color_pair(ART)
        )
    
