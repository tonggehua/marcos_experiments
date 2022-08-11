import numpy as np
import matplotlib.pyplot as plt
import pdb
st = pdb.set_trace

import external # imports external.py
import marcos_client.experiment as ex

def my_first_experiment():
    exp = ex.Experiment(lo_freq=5,rx_t=3.125)# 5 MHz mod/demod frequency; 3.125 us Rx sampling interval

    # Define Tx0 parameters
    tx0_times = np.array([50, 130]) # Absolute times
    tx0_amps = np.array([0.5, 0]) # Output values (0-1, or 0%-100%)

    # Add Tx0 entry to event dictionary
    event_dict = {'tx0': (tx0_times, tx0_amps)}

    # Add events to experiment
    exp.add_flodict(event_dict)

    exp.add_flodict({'rx0_en': (np.array([200,400]),np.array([1,0]))})
    #
    # exp.plot_sequence()
    # plt.show()

    # Run experiments
    rxd, msgs = exp.run()
    # Close emulator (but not server on hardware)
    exp.close_server(only_if_sim=True)

def my_second_experiment():
    exp = ex.Experiment(lo_freq=5, rx_t=3.125)
    event_dict = {'tx0': (np.array([50,130,200,360]),np.array([0.5,0,0.5j,0])),
                  'tx1': (np.array([500,700]),np.array([0.2,0])),
                  'rx0_en': (np.array([400,800]),np.array([1,0])),
                  'rx1_en': (np.array([400,800]),np.array([1,0]))}
    exp.add_flodict(event_dict)
    exp.plot_sequence()

    rxd, msgs = exp.run()
    # rxd contains raw readout data.
    # With the emulator, a loopback is mimicked and
    # Rx0 measures Tx0 while Rx1 measures Tx1


    exp.close_server(only_if_sim=True)

    plt.figure()
    plt.plot(np.absolute(rxd['rx1']))
    plt.show()

if __name__ == "__main__":
    #my_first_experiment()
    my_second_experiment()