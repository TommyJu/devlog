import curses
from ui.ui_constants import STATUS_PAUSED_COLOR_ID, STATUS_RUNNING_COLOR_ID, PADDING_X, PADDING_Y
from ui.display_art import display_art

# Layout
START_DATETIME_Y = 1
STATUS_Y = 2
ELAPSED_SECONDS_Y = 3




def render_timer(timer, stdscr):
    display_art(stdscr)
    display_controls(stdscr)
    
    start_datetime = timer.get_formatted_start_datetime()
    display_start_datetime(stdscr, start_datetime)
    
    if timer.paused:
        display_program_status(stdscr, False)
        elapsed_seconds = timer.get_formatted_elapsed_seconds()
        display_elapsed_seconds(stdscr, elapsed_seconds, False)
    else:
        display_program_status(stdscr, True)
        elapsed_seconds = timer.get_formatted_elapsed_seconds()
        display_elapsed_seconds(stdscr, elapsed_seconds, True)
        
# Helper Functions --------------------
def display_controls(stdscr):
    height, width = stdscr.getmaxyx()
    controls = "[Q] End Session  [SPACE] Pause/Resume"
    stdscr.addstr(height - PADDING_Y, PADDING_X, controls[:width - PADDING_X])
    
def display_program_status(stdscr, is_running):
    if is_running:
        stdscr.addstr(STATUS_Y, PADDING_X, "Program Status: RUNNING", curses.color_pair(STATUS_RUNNING_COLOR_ID))
    else:
        stdscr.addstr(STATUS_Y, PADDING_X, "Program Status: PAUSED", curses.color_pair(STATUS_PAUSED_COLOR_ID))
    
    
def display_elapsed_seconds(stdscr, message, is_running):
    if is_running:  
        stdscr.addstr(ELAPSED_SECONDS_Y, PADDING_X, f"Elapsed Time: {message}", curses.A_ITALIC)
    else:
        stdscr.addstr(ELAPSED_SECONDS_Y, PADDING_X, f"Elapsed Time: {message}", curses.A_ITALIC | curses.A_BLINK)
        
def display_start_datetime(stdscr, message):
    stdscr.addstr(START_DATETIME_Y, PADDING_X, f"Session Start: {message}", curses.A_DIM)
    
