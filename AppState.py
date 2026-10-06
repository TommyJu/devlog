from time import time

class AppState:
    def __init__(self):
        self.running = True
        self.paused = False
        self.window_resized = False
        self.start = time()
        self.elapsed_accumulated = 0
        
    def get_elapsed_time(self):
        if self.paused:
            elapsed = int(self.elapsed_accumulated)
        else:
            elapsed = int(
                self.elapsed_accumulated +
                time() - self.start
            )

        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"Elapsed: {hours:02}:{minutes:02}:{seconds:02}"