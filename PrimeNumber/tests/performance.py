from memory_profiler import profile, memory_usage
from src.index import PrimeNumbers
import random
import timeit


@profile
def metricPrimeNumbers():
    PrimeNumbers(random.randrange(1,50))


if __name__ == "__main__":
    execution_time = timeit.timeit(metricFunction, number=1)
    print(f"Execution time: {execution_time}")
