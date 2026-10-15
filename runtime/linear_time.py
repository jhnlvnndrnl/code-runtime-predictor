import time

def calculate_sum(numbers):
    total = 0

    # Time complexity: O(n), where n is the list length.
    for number in numbers:
        total += number

    return total

numbers = list(range(100_000))

start = time.perf_counter()

result = calculate_sum(numbers)

end = time.perf_counter()

# Runtime measures only the calculate_sum() function call.
runtime = end - start

print("Result:", result)
print(f"Execution time: {runtime:.8f} seconds")