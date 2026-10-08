from time import time
from datetime import datetime


class Timer:
    def __init__(self):
        self.paused = False
        self.start = time()
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self.elapsed_seconds = 0

    def toggle_pause(self):

        if self.paused:
            # Start a new timing period
            self.start = time()
            self.paused = False

        else:
            # Add current timing period to total
            self.elapsed_seconds += time() - self.start
            self.paused = True

    def stop_timer(self):
        if not self.paused:
            # Add the final timing period
            self.elapsed_seconds += time() - self.start

        self.end_datetime = datetime.now()

    def get_formatted_elapsed_seconds(self):
        # Elapsed time if paused or session ended
        if self.end_datetime is not None or self.paused:
            elapsed = int(self.elapsed_seconds)
        
        # Elapsed time while timer is running
        else:
            elapsed = int(
                self.elapsed_seconds +
                time() - self.start
            )

        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def get_formatted_start_datetime(self):
        return self.start_datetime.strftime("%A, %B %-d, %Y at %-I:%M %p")
    
    def get_formatted_end_datetime(self):
            return self.end_datetime.strftime("%A, %B %-d, %Y at %-I:%M %p")