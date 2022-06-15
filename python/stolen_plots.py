import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft , rfft, irfft , fftfreq
from numpy import exp, log, log10, cos, sin, pi, cosh, sinh , sqrt
from classySInuPT import Class
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

'''
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
                    'alpha_s': 0
                    }

M = Class()
M.set(common_settings)
M.set({ 'output': 'mPk',
        'cb': 'Yes'
        })
M.compute()
'''

z_pk = 0.61
common_settings = {# fixed LambdaCDM parameters
                   'A_s':2.089e-9,
                   'n_s':0.9649,
                   'tau_reio':0.052,
                   'omega_b':0.02237,
                   'omega_cdm':0.12,
                   'h':0.6736,
                   'YHe':0.2425,
#                     'N_eff':3.046,
                    'N_ur':2.0328,
                    'N_ncdm':1,
                    'm_ncdm':0.06,
                   # other output and precision parameters
#                    'P_k_max_1/Mpc':100.0,
                   'z_pk':z_pk}  

M = Class()
M.set(common_settings)
#let's first take a look at the one-loop power spectrum for matter without IR resummation
M.set({ 'output':'mPk',
       'non linear':'PT',
       'IR resummation':'No',
       'Bias tracers':'No'
       ,'cb':'Yes'
      })
M.compute()
#now we compute all the spectra including IR resummation, RSD, 
#and AP generated for a fiducial cosmology with $\Omega_m=0.31$ 
M1 = Class()
M1.set(common_settings)
M1.set({'output':'mPk',
        'non linear':'PT',
        'IR resummation':'Yes',
        'Bias tracers':'Yes',
        'cb':'Yes',
        'RSD':'Yes',
        'AP':'Yes',
        'Omfid':'0.31'
       })
M1.compute()

font = {'size'   : 20, 'family':'STIXGeneral'}
axislabelfontsize='large'
matplotlib.rc('font', **font)
matplotlib.mathtext.rcParams['legend.fontsize']='small'
plt.rcParams["figure.figsize"] = [8.0,6.0]


#############################################
#
# extract spectra and plot them
#
#############################################

h = M.h()
fz = M.scale_independent_growth_factor_f(z_pk)
kvec = np.logspace(-3,np.log10(3),1000) # array of kvec in h/Mpc
twopi = 2.*math.pi
khvec = kvec*h # array of kvec in 1/Mpc
#
# Create figures
#
fig_Pk, ax_Pk = plt.subplots()
fig_Pkir, ax_Pkir = plt.subplots()
fig_Pkgg, ax_Pkgg = plt.subplots()
fig_Pkgm, ax_Pkgm = plt.subplots()
fig_Pkmz, ax_Pkmz = plt.subplots()
fig_Pkgz, ax_Pkgz = plt.subplots()


##### NUISANCE PARAMETERS ####
b1 = 2.0
cs = 1. # in units [Mpc/h]^2
b2 = -1.
bG2 = 0.1
bGamma3 = -0.1
Pshot = 5e3 # in units [Mpc/h]^3
cs0 = 5. # in units [Mpc/h]^2
cs2 = 15. # in units [Mpc/h]^2
cs4 = -5. # in units [Mpc/h]^2
b4 = 100. # in units [Mpc/h]^4
##############################

## Initialize the convenience functions pk_mm_real, pk_gg_l0 etc.
M.initialize_output(khvec, z_pk, len(khvec))
M1.initialize_output(khvec, z_pk, len(khvec))

## COMPUTE SPECTRA #######
# NB: these are fast, since no quantities are recomputed

# basic real space matter power spectrum without IR resummation
pk_full = M.pk_mm_real(cs)

# real space matter power spectrum
pk_full_ir = M1.pk_mm_real(cs)

# real space galaxy-galaxy power spectrum 
#pk_gg = M1.pk_gg_real(b1, b2, bG2, bGamma3, cs, cs0, Pshot)

# real space galaxy-matter power spectrum 
#pk_gm = M1.pk_gm_real(b1, b2, bG2, bGamma3, cs, cs0)

# dark matter redshift space monopole/quadrupole/hexadecapole
#pk_m0 = M1.pk_mm_l0(cs0)
#pk_m2 = M1.pk_mm_l2(cs2)
#pk_m4 = M1.pk_mm_l4(cs4)

# galaxy redshift space monopole/quadrupole/hexadecapole
#pk_g0 = M1.pk_gg_l0(b1, b2, bG2, bGamma3, cs0, Pshot, b4)
#pk_g2 = M1.pk_gg_l2(b1, b2, bG2, bGamma3, cs2, b4)
#pk_g4 = M1.pk_gg_l4(b1, b2, bG2, bGamma3, cs4, b4)
###########################

# Compute additional quantities (which don't have inbuilt wrappers)

# linear theory matter power spectrum
#pk_lin = np.asarray([M1.pk_lin(kh,z_pk)*h**3. for kh in khvec])

# load all non-linear components
M1_mult = M1.get_pk_mult(khvec, z_pk, len(khvec))
M_mult = M.get_pk_mult(khvec, z_pk, len(khvec))

# separate contributions of the matter-matter power spectrum
pk_tree = M_mult[14]*h**3.
pk_loop = M_mult[0]*h**3.
pk_ctr = 2*M_mult[10]*h
# separate contributions of the galaxy-galaxy power spectrum
#pk_Id2 = (M1_mult[2])*h**3.
#pk_IG2 = (M1_mult[3])*h**3. 
#pk_Id2d2 = (M1_mult[1])*h**3. 
#k_IG2G2 = (M1_mult[5])*h**3. 
#pk_Id2G2 = (M1_mult[4])*h**3. 
#pk_FG2 = (M1_mult[6])*h**3.
    
ax_Pk.loglog(kvec,np.array(np.abs(pk_loop)),color='purple',linestyle='-',label='1-loop')
ax_Pk.loglog(kvec,np.array(np.abs(pk_ctr)),color='b',linestyle='-',label='Counterterm')
ax_Pk.loglog(kvec,np.array(pk_tree),color='darkorange',linestyle='-',label='Linear')
ax_Pk.loglog(kvec,np.array(pk_full),color='darkgreen',linestyle='-',label='Total')



ax_Pk.set_xlim([1.e-3,1])
ax_Pk.set_ylim([1,5e4])
ax_Pk.set_xlabel(r'$k \,\,\,\, [h\mathrm{Mpc}^{-1}]$')
ax_Pk.set_ylabel(r'$P(k)\,\,\,\, [h^{-1}\mathrm{Mpc}]^3$')
ax_Pk.legend(fontsize='16',ncol=1,loc='upper left')
fig_Pk.savefig('from_notebookcode_real_Pk.pdf')
fig_Pk.tight_layout()
