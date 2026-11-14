from memory_profiler import profile
from profiler import slow_function, fast_function, memory_intensive_function


@profile
def main():
    slow_function()
    fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
