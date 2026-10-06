import curses

def initialize_ui(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.nodelay(True)
    display_controls(stdscr)
    
def render(app_state, stdscr):
    if app_state.window_resized:
        stdscr.clear()
        display_controls(stdscr)
        app_state.window_resized = False
    elif app_state.paused:
        display_paused_text(stdscr)
    elif not app_state.paused:
        elapsed_time = app_state.get_elapsed_time()
        display_elapsed_time(stdscr, elapsed_time)

# Helper Functions ---------------------
def update_text(stdscr, message):
    stdscr.move(1, 1)
    stdscr.clrtoeol()
    stdscr.addstr(message, curses.color_pair(1))
    
def display_controls(stdscr):
    height, width = stdscr.getmaxyx()
    controls = "[Q] Quit  [SPACE] Pause/Resume"
    stdscr.addstr(height - 2, 1, controls[:width - 1])
    
def display_paused_text(stdscr):
    stdscr.move(1, 1)
    stdscr.clrtoeol()
    stdscr.addstr("PAUSED", curses.color_pair(1))
    
def display_elapsed_time(stdscr, message):
    stdscr.move(1, 1)
    stdscr.clrtoeol()
    stdscr.addstr(message, curses.color_pair(1))
    
