import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/john/Downloads/CLASS_SInu-master/output/mless_LCDM_km5_pk.dat', '/home/john/Downloads/CLASS_SInu-master/output/mless_2Geff2_km5_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['mless_LCDM_km5_pk', 'mless_2Geff2_km5_pk']

fig, ax = plt.subplots()
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()
fig.savefig('Plots/mless_2Geff_2_km5.png')