from ui.display_art import display_art
from ui.ui_constants import PADDING_X, PADDING_Y


def render_session_notes(stdscr, notes):
    display_art(stdscr)

    height, width = stdscr.getmaxyx()

    prompt = "Optional session notes [Enter] to save:"
    input_width = width - (PADDING_X * 2)

    stdscr.addstr(
        height - PADDING_Y - 1,
        PADDING_X,
        prompt[:input_width]
    )

    # Leave room for the cursor
    visible_width = input_width - 1

    # Show the end of the string if it is too long
    visible_notes = notes[-visible_width:]

    stdscr.addstr(
        height - PADDING_Y,
        PADDING_X,
        visible_notes
    )

    # Put cursor after the visible text
    cursor_x = PADDING_X + len(visible_notes)

    stdscr.move(
        height - PADDING_Y,
        min(cursor_x, width - 1)
    )