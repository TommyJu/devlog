from ascii_art import ASCII_ART
from ui.ui_constants import ART_COLOR_ID, ART_Y, PADDING_X, PADDING_Y
from curses import color_pair

def display_art(stdscr):

    height, width = stdscr.getmaxyx()

    controls_y = height - PADDING_Y

    for row, line in enumerate(ASCII_ART.splitlines()):

        current_y = ART_Y + row

        # Don't draw into the controls area
        if current_y >= controls_y:
            break

        # Clip the right side if necessary
        available_width = width - PADDING_X

        if available_width <= 0:
            break

        stdscr.addstr(
            current_y,
            PADDING_X,
            line[:available_width],
            color_pair(ART_COLOR_ID)
        )