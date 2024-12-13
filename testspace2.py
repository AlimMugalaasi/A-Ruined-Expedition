
import time, os
os.system('clear')

for i in range(5):
    print(f"\rCounting: {i}", end="", flush=True)
    time.sleep(1)  # Pause for visibility
    print("\r" + " " * 20, end="", flush=True)  # Clear the line