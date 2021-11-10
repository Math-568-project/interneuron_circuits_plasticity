import numpy as np
import multiprocessing
from brian2 import *
from sacred.observers import FileStorageObserver
from Spiking_model import ex
import sys

sys.setrecursionlimit(20)
ex.observers.append(FileStorageObserver.create('Spiking_model'))
ex.run('run_network')
"""
def run_in_thread(values):
    from Spiking_model import ex
    ex.observers.append(FileStorageObserver.create('Spiking_model'))
    ex.run('run_network')


values1 = np.array([0])
n_threads = len(values1)
pool = multiprocessing.Pool(n_threads)
pool.map(run_in_thread, values1)
"""