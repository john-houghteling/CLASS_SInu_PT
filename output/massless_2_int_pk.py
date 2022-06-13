import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/john/Downloads/CLASS_SInu-master/output/massless_2_int_pk.dat', '/home/john/Downloads/CLASS_SInu-master/output/mless_2_int_1G_eff_pk.dat', '/home/john/Downloads/CLASS_SInu-master/output/LCDM_massless_nu_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['massless_2_int_pk', 'mless_2_int_1G_eff_pk', 'LCDM_massless_nu_pk']

fig, ax = plt.subplots()
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()