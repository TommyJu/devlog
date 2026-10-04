import time
import curses

def update_text(stdscr, message):
    stdscr.move(1, 1)
    stdscr.clrtoeol()
    stdscr.addstr(message, curses.color_pair(1))

def get_elapsed_time(start, elapsed_before_pause):
    elapsed = int(elapsed_before_pause + (time.time() - start))

    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"Elapsed: {hours:02}:{minutes:02}:{seconds:02}"

def display_controls(stdscr):
    height, width = stdscr.getmaxyx()
    controls = "[Q] Quit  [SPACE] Pause/Resume"
    stdscr.addstr(height - 2, 1, controls[:width - 1])

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.nodelay(True)
    

    running = True
    paused = False

    start = time.time()
    elapsed_before_pause = 0

    display_controls(stdscr)
    while running:
        key = stdscr.getch()
        
        if key == curses.KEY_RESIZE:
            stdscr.clear()
            display_controls(stdscr)

        if key == ord(" "):
            if not paused:
                # Save the time accumulated before pausing
                elapsed_before_pause += time.time() - start
                paused = True
                update_text(stdscr, "PAUSED")

            else:
                # Start a new timing period
                start = time.time()
                paused = False

        elif key == ord("q"):
            running = False

        elif not paused:
            elapsed_time = get_elapsed_time(start, elapsed_before_pause)
            update_text(stdscr, elapsed_time)

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)