import time

# This is a simple script to measure how fast Python handles data.
# Measuring speed (benchmarking) is a key requirement for the DUNE project.

# 1. Capture the start time
start_time = time.time()

# 2. The task: Create a list with 1,000,000 numbers
data = []
for i in range(1000000):
    data.append(i)

# 3. Capture the end time
end_time = time.time()

# 4. Calculate and print the result
total_time = end_time - start_time
print(f"Time taken to process 1,000,000 items: {total_time:.6f} seconds")
