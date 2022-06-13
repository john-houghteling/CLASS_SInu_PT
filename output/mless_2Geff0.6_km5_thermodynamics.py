import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/john/Downloads/CLASS_SInu-master/output/mless_2Geff0.6_km5_thermodynamics.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['mless_2Geff0']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'sum_g_idm_dr[Mpc^-1]']
tex_names = ['sum_g_idm_dr [Mpc^-1]']
x_axis = 'conf. time [Mpc]'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 7])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('conf. time [Mpc]', fontsize=16)
plt.show()
fig.savefig('mless_2Geff0.6_km5_g.png')