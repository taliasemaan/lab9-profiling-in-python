import time
import unittest

import memory_profiler

from optimized_profiler import (
    memory_intensive_function,
    optimized_fast_function,
    slow_function,
)


class TestOptimizedProfiler(unittest.TestCase):
    def time_function(self, func):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    def test_slow_function(self):
        duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.2f} seconds.")
        self.assertGreater(duration, 2, "slow_function should take more than 2 seconds.")

    def test_fast_function(self):
        duration = self.time_function(optimized_fast_function)
        print(f"optimized_fast_function executed in {duration:.2f} seconds.")
        self.assertLess(
            duration, 1, "optimized_fast_function should take less than 1 second."
        )

    def test_memory_intensive_function(self):
        mem_usage_before = memory_profiler.memory_usage()[0]
        duration = self.time_function(memory_intensive_function)
        mem_usage_after = memory_profiler.memory_usage()[0]

        print(f"memory_intensive_function executed in {duration:.2f} seconds.")
        print(
            f"Memory usage before: {mem_usage_before:.2f} MiB, after: {mem_usage_after:.2f} MiB."
        )

        self.assertLess(duration, 5, "memory_intensive_function should take less than 5 seconds.")
        self.assertGreater(mem_usage_after, mem_usage_before, "Memory usage should increase after running memory_intensive_function.")


if __name__ == "__main__":
    unittest.main()
