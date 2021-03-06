#!/usr/bin/env python3
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self, type, value, traceback):
        self.finish_time = time.time()
        print("Elapsed time: " + str((self.finish_time - self.start_time) * 1000) + " msecs.")
        return False


if __name__ == "__main__":
    with Timer():
        time.sleep(0.5)

    with Timer():
        b = 1
        for i in range(1000, 800000):
            b *= i + 10
            b /= i - 19
