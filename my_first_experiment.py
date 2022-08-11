import numpy as np
import matplotlib.pyplot as plt
import pdb
st = pdb.set_trace

import external # imports external.py
import marcos_client.experiment as ex

def my_first_experiment():
    exp = ex.Experiment(lo_freq=5,rx_t=3.125)# 5 MHz mod/demod frequency; 3.125 us Rx sampling interval

if __name__ == "__main__":
    my_first_experiment()