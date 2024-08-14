import os
import multiprocessing
from keep_alive import keep_alive


def run_gungnir():
  os.system("~/go/bin/gungnir -r roots.txt | notify")


process1 = multiprocessing.Process(target=run_gungnir)
process2 = multiprocessing.Process(target=keep_alive)
process1.start()
process2.start()
process1.join()  # Wait for process1 to finish
process2.join()
