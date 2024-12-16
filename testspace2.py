import time, random
from rich.progress import track
from ExtraFunctions import printc

for i in track(range(100), description=printc('LOADING GAME ASSETS...', 'bold green' )):
    timing = random.uniform(0.01, 0.3)
    time.sleep(timing)