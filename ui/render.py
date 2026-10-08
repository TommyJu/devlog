import curses
from ui.ui_constants import (
    STATUS_RUNNING_COLOR_ID,
    STATUS_PAUSED_COLOR_ID,
    TEXT_COLOR_ID,
    ART_COLOR_ID,
    STATUS_RUNNING_COLOR,
    STATUS_PAUSED_COLOR,
    TEXT_COLOR,
    ART_COLOR,
    BACKGROUND_COLOR,
)

from ui.render_timer import render_timer
from ui.render_save_session import render_save_session
from ui.render_session_notes import render_session_notes
from ScreenState import ScreenState


def initialize_ui(stdscr):
    curses.start_color()
    stdscr.nodelay(True)
    curses.init_pair(STATUS_RUNNING_COLOR_ID, STATUS_RUNNING_COLOR, BACKGROUND_COLOR)
    curses.init_pair(STATUS_PAUSED_COLOR_ID, STATUS_PAUSED_COLOR, BACKGROUND_COLOR)
    curses.init_pair(TEXT_COLOR_ID, TEXT_COLOR, BACKGROUND_COLOR)
    curses.init_pair(ART_COLOR_ID, ART_COLOR, BACKGROUND_COLOR)
    stdscr.bkgd(" ", curses.color_pair(TEXT_COLOR_ID))
    
    
def render(stdscr, app_state):
    stdscr.erase()
    
    if app_state.screen == ScreenState.TIMER:
        render_timer(app_state.timer, stdscr)
        
    if app_state.screen == ScreenState.SAVE_SESSION:
        render_save_session(stdscr)
        
    if app_state.screen == ScreenState.SESSION_NOTES:
        render_session_notes(stdscr, app_state.session_notes)
        

    
