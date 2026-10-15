import time

def count_pairs(n):
    count = 0

    # Time complexity: O(n^2), because n * n = n^2 operations.
    for i in range(n):
        for j in range(n):
            count += 1

    return count

n = 1000

start = time.perf_counter()

result = count_pairs(n)

end = time.perf_counter()

runtime = end - start

print("Result:", result)
print(f"Execution time: {runtime:.8f} seconds")