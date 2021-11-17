import numpy as np


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def calc_impact(con_REC):
    pop1impact = np.mean(con_REC['i<100 and j>100'])
    otherimpact = (np.mean(con_REC['i>100 and i<300 and j>300']) +
                   np.mean(con_REC['i>200 and j>100 and j<200']) +
                   np.mean(con_REC['i>100 and i<200 and j>200 and j<300']) +
                   np.mean(con_REC['i>300 and j>200 and j<300'])) / 4
    self_impact = (np.mean(con_REC['i<100 and j<100']) +
                   np.mean(con_REC['i>100 and i<200 and j>100 and j<200']) +
                   np.mean(con_REC['i>200 and i<300 and j>200 and j<300']) +
                   np.mean(con_REC['i>300 and i<400 and j>300 and j<400'])) / 4
    impact_normtoself = (pop1impact - otherimpact) / self_impact
    impact_normtomax = (pop1impact - otherimpact) / np.max(con_REC)
    print("impact")

    return impact_normtoself, impact_normtomax


def mean_phase_cohearence(spike_times_a, spike_times_b):
    # calculate the mean phase coherence between two spike trains
    mean_sin = 0
    mean_cos = 0
    count = 0
    if not (spike_times_a and spike_times_b):
        return None
    for spike_time_a in spike_times_a:
        spike_time_b_2, idx = next(
            ((spike_time_b, idx)
             for (idx, spike_time_b) in enumerate(spike_times_b)
             if spike_time_b > spike_time_a), (0, 0))
        if idx == 0:
            continue
        count += 1
        spike_time_b_1 = spike_times_b[idx - 1]
        phase = 2 * np.pi * (spike_time_a - spike_time_b_1) / (spike_time_b_2 -
                                                               spike_time_b_1)
        mean_sin += np.sin(phase)
        mean_cos += np.cos(phase)
    mean_sin /= count
    mean_cos /= count
    return (mean_sin**2 + mean_cos**2)**0.5
