import time
from standardlife import standard_life_runner


def main() -> None:
    start_time = time.perf_counter()
    standard_life_runner()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
