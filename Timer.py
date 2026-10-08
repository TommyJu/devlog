from time import time
from datetime import datetime


class Timer:
    def __init__(self):
        self.paused = False
        self.start = time()
        self.start_datetime = datetime.now()
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

        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def get_start_datetime(self):
        return self.start_datetime.strftime("%A, %B %-d, %Y at %-I:%M %p")