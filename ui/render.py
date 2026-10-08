import curses
from curses.textpad import Textbox
from ui.ui_constants import STATUS_PAUSED_COLOR_ID, STATUS_RUNNING_COLOR_ID, TEXT_COLOR_ID, ART_COLOR_ID, ART_Y, PADDING_X, PADDING_Y

from ui.render_timer import render_timer
from ScreenState import ScreenState


def initialize_ui(stdscr):
    curses.start_color()
    stdscr.nodelay(True)
    curses.init_pair(STATUS_RUNNING_COLOR_ID, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(STATUS_PAUSED_COLOR_ID, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(TEXT_COLOR_ID, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(ART_COLOR_ID, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.bkgd(" ", curses.color_pair(TEXT_COLOR_ID))
    
    
def render(stdscr, app_state):
    stdscr.erase()
    
    if app_state.screen == ScreenState.TIMER:
        render_timer(app_state.timer, stdscr)
        
    ...
        
    

# Helper Functions ---------------------
def ask_to_save_session(stdscr):
    ...
        
def ask_for_notes(stdscr):
    ...
    
