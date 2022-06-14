import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft , rfft, irfft , fftfreq
from numpy import exp, log, log10, cos, sin, pi, cosh, sinh , sqrt
from classy import Class
from scipy.optimize import fsolve
from scipy.special import gamma
from scipy.special import hyp2f1
from scipy import interpolate
import sys,os
from time import time
from scipy.integrate import quad
import scipy.integrate as integrate
from scipy import special
from scipy.special import factorial
import math


common_settings = { 
                    'H0': 67.32,
                    'T_cmb': 2.7255,
                    'YHe': 0.2453,
                    'omega_b': 0.022383,
                    'Omega_k': 0.,
                    'omega_cdm': 0.12011,
                    'tau_reio': 0.0543,
                    'l_max_scalars': 2500,
                    'N_ncdm': 0,
                    'N_ur': 3.046,
                    'ln10^{10}A_s': 3.0448,
                    'n_s': 0.96605,
                    'alpha_s': 0,
                    'l_max_idr': 17
                    }

M = Class()
M.set(common_settings)
M.set({ 'output': 'mPk',
        'cb': 'Yes'
        })
M.compute()
