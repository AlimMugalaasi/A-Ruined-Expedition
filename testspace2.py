import time, random
from rich.progress import track
from ExtraFunctions import printc

for i in track(range(20), description=printc('LOADING...', 'bold green' )):
    timing = random.uniform(0.1, 0.9)
    time.sleep(timing)