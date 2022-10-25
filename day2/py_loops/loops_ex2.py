import time

now = time.time()

print("Waiting for 15 seconds...")
while (time.time() - now) <= 15:
    time.sleep(1)
    elapsed_time = time.time() - now
    print(f"still waiting...{elapsed_time:.1f}s")

elapsed_time = time.time() - now
print(f"Done: {elapsed_time:.1f}s")
