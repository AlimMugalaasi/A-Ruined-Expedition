import time, os

script_start_time = time.time()


while True:
    os.system('clear')
    current_time = time.time()
    runtime = current_time - script_start_time
    print(f"Script runtime: {runtime:.2f} seconds")