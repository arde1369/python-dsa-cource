from functools import lru_cache
import time

@lru_cache(128)
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

#first run. saves results
start = time.time()
result = fib(100)
end= time.time()
print(f"Result: {result}, Time taken: {end - start:.10f} seconds")

#second time called with the same n. will return results from cache
start = time.time()
result = fib(20)
end= time.time()
print(f"Result: {result}, Time taken: {end - start:.10f} seconds")