import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/john/Downloads/CLASS_SInu-master/output/mless_2Geff2_km5_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['mless_2Geff2_km5_pk']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 1])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()
fig.savefig('Plots/mless_2Geff_2_km5.png')