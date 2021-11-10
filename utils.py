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