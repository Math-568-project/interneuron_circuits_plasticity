from brian2 import *

params = {
    # enables plotting during the run
    'plot': False,
    # random seed
    'seed': 7472,
    # no plasticity, to measure tuning
    'nonplasticwarmup_simtime': 1.4 * second,
    # plasticity, no reward
    'warmup_simtime': 42 * second,
    # plasticity, with reward
    'reward_simtime': 24.5 * second,
    # plasticity, without reward
    'noreward_simtime': 45 * second,
    # plasticity, without reward
    # for Suppl. Figure, we killed SSTPV structure after 45s, therefore the no reward simtime is split up
    'noSSTPV_simtime': 21 * second,
    # no plasticity, to measure tuning
    'after_simtime': 1.4 * second,
    'timestep': 0.1 * ms,

    # number of neurons
    # Number of excitatory L23 PYR cells
    'NPYR': 400,
    # Number of inhibitory SOM cells
    'NSOM': 30 * 4,
    # Number of inhibitory VIP cells
    'NVIP': 50,
    # Number of inhibitory PV cells
    'NPV': 120,
    # Number of top-down units
    'NTD': 100,

    # time constants of synaptic kernels
    # Excitatory synaptic time constant
    'tau_ampa': 5.0 * ms,
    # Inhibitory synaptic time constant
    'tau_gaba': 10.0 * ms,

    # L4 input
    # Number of L4 units
    'N4': 4,
    # Firing rate of L4 units
    'L4_rate': 4 / (1 * ms),
    # Four orientations
    'orientations':
    np.array([0.785398163397, 1.57079632679, 2.35619449019, 0.0]),
    # stim_time + gap_time, i.e. time between starts of two subsequent stimuli
    'input_time': 70 * ms,
    # duration of stimulus
    'stim_time': 50 * ms,

    # L23 neuron parameters
    # Leak conductance
    'gl': 10.0 * nsiemens,
    # Resting potential
    'el': -60 * mV,
    # Inhibitory reversal potential
    'er': -80 * mV,
    # Spiking threshold
    'vt': -50. * mV,
    # Membrane capacitance
    'memc': 200.0 * pfarad,
    # sigma of Ornstein-Uhlenbeck noise
    'sigma': 2.0 * mV,
    # tau of Ornstein-Uhlenbeck noise
    'tau_noise': 5.0 * ms,

    # Connectivity

    #p_pre_post is the probability of connection from a neuron in the presynaptic population to a neuron in the postsynaptic population
    #w_pre_post is the synaptic strength of the connection from a neuron in the presynaptic population to a neuron in the postsynaptic population
    'p_PYR_PYR': 1.0,
    # initial weights between PCs
    'recurrent_weights': 'clip(.01 * randn() + .01, 0, .15)*nS',
    'p_SOM_PV': .857,
    # initial weights between SST and PV
    'SOM2PV_weights': 'clip(.1 * randn() + .2, 0, 1.0)*nS',
    'p_L4_TD': 1.0,
    'p_TD_VIP': 1.0,
    'p_PYR_SOM': 1.0,
    'p_PYR_VIP': 1.0,
    'p_PYR_PV': .88,
    'p_SOM_PYR': 1.0,
    'p_SOM_VIP': 1.0,
    'p_PV_PV': 1.0,
    'p_VIP_SOM': 1.0,
    'p_VIP_PYR': .125,
    'p_VIP_PV': .125,
    'p_PV_SOM': .125,
    'p_PV_PYR': 1.0,
    'p_PV_VIP': 1.0,
    'p_VIP_VIP': .125,
    'p_SOM_SOM': .125,
    'w_PYR_SOM': 0.07 * nS,
    'w_PYR_VIP': 0.07 * nS,
    'w_PYR_PV': .12 * nS,
    'w_SOM_PYR': 0.3 * nS,
    'w_SOM_VIP': 0.42 * nS,
    'w_PV_PV': 0.55 * nS,
    'w_VIP_SOM': 0.195 * nS,
    'w_PV_SOM': 0.08 * nS,
    'w_PV_PYR': 0.55 * nS,
    'w_PV_VIP': 0.12 * nS,
    'w_VIP_PYR': .0675 * nS,
    'w_VIP_PV': .0675 * nS,
    'w_VIP_VIP': .0 * nS,
    'w_SOM_SOM': .0675 * nS,
    'w_L4PYR': .28 * nS,
    'w_FFPYR': .13 * nS,
    'w_FFPV': .01 * nS,
    'w_FFSOM': .15 * nS,
    'w_TDVIP': .2 * nS,

    # gap junction parameters
    # sub-threshold coupling
    'w_gap': 0 * nS,
    # spikelet current
    'c_gap': 13 * pA,
    'tau_spikelet': 9.0 * ms,  # spikelet time constant

    # Plasticity parameters
    # STDP time constant at excitatory synapses
    'tau_stdp': 20 * ms,
    # STDP time constant at inhibitory synapses
    'tau_istdp': 20 * ms,
    # STDP amplitude
    'dApre': .005,
    # Inhibitory STDP amplitude
    'dApre_i': 0.015,
    # maximum synaptic weight for excitatory synapses
    'gmax': .25 * nS,
    # maximum synaptic weight for SST-to-PV synapses
    'gmax_SSTPV': 1.0 * nS,
    # maximum synaptic weight bound relative to initial weight
    'relbound': .1,
    # if True all connections are plastic
    'restplastic': False,
}
