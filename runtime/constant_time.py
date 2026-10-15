import time

def get_first(numbers):
    # Time complexity: O(1), because list indexing is constant time.
    return numbers[0]

numbers = list(range(100_000))

# Start measuring execution time.
start = time.perf_counter()

result = get_first(numbers)

# Stop measuring execution time.
end = time.perf_counter()

# Calculate elapsed time in seconds.
runtime = end - start

print("Result:", result)
print(f"Execution time: {runtime:.8f} seconds")