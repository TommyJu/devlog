from time import time

def handle_key_events(app_state, key):
    if key == ord(" "):
        if not app_state.paused:
            # Save the time accumulated before pausing
            app_state.elapsed_accumulated += time() - app_state.start
            app_state.paused = True

        else:
            # Start a new timing period
            app_state.start = time()
            app_state.paused = False

    elif key == ord("q"):
        app_state.running = False