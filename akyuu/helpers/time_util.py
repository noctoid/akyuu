import time

def get_current_epoch_time_in_ms() -> int:
    return int(time.time() * 1000)
