import time
import functools
from halo import Halo


__all__ = ["timer"]

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        spinner = Halo(text=f'Running {func.__name__!r} function...', spinner='dots')
        spinner.start()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time_sec = end_time - start_time    # 3
        run_time_min = run_time_sec/60
        spinner.stop()
        print('')
        print(f'Finished {func.__name__!r} in {run_time_sec:.4f} secs\n')
        print(f'Finished {func.__name__!r} in {run_time_min:.4f} min')
        return value
    return wrapper_timer