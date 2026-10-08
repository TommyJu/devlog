from ui.display_art import display_art
from ui.ui_constants import PADDING_X, PADDING_Y

def render_save_session(stdscr):
    display_art(stdscr)
    height, width = stdscr.getmaxyx()

    message = "Save session in dev log? [Y] Yes  [N] No"

    stdscr.addstr(
        height - PADDING_Y,
        PADDING_X,
        message[:width - PADDING_X]
    )