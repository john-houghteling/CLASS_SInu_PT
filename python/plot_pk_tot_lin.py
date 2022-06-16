import matplotlib.pyplot as plt
import numpy as np

# set true to plot ratio of files
ratio = False

#speed of sound?? cs with same value as in notebook
cs = 1 #(Mpc/h)^2
h = 0.6732

# add all files to be considered here, may make argv later, if using ratio, 1st will be the norm
filename = ["../output/mless_LCDM_PT_km100_pk.dat", "../output/mless_LCDM_PT_km100_pk_nl_pt.dat"]
names = []
dat = []

# read files
for i in range(0, len(filename)):
    with open(filename[i], 'r') as f:
        dat.append(f.readlines())

# remove file headers
for i in range(0, 4):
    for j in range(0,len(dat)):
        dat[j].pop(0)

# separate different variables within each row
for i in range(0, len(dat)):
    for j in range(0, len(dat[i])):
        dat[i][j] = dat[i][j].split()

#print(dat[1][0][9]) #tree
#print(dat[1][0][2]) #ctr

# turn everything into np arrays bc theyre nice to do math with
# our goal is to print pk, tree, tot
k_arr = np.empty(len(dat[0]))
pk_arr = np.empty(len(dat[0]))
tree_arr = np.empty(len(dat[0]))
ctr_arr = np.empty(len(dat[0]))
for i in range(0, len(dat[0])):     
    k_arr[i] = dat[0][i][0]
    pk_arr[i] = dat[0][i][1]
    tree_arr[i] = dat[1][i][9]
    ctr_arr[i] = dat[1][i][2]
tot_arr = (pk_arr - (2*cs/h**2)*ctr_arr)*h**3
pk_arr = pk_arr*h**3
tree_arr = tree_arr*h**3

# divide for ratio plot if needed
if ratio:
    tree_arr = np.divide(tree_arr, pk_arr)
    tot_arr = np.divide(tot_arr, pk_arr)
    pk_arr = np.divide(pk_arr,pk_arr)

#print(tot_arr)
#print(tree_arr)
# plot and save
plt.title("$P_k$ ratio")
plt.xlabel("k [h/Mpc]")
plt.ylabel("$P_{k, i}/P_{k, LCDM}$")
plt.xlim(0.001, 10.)
#plt.ylim(0.,2.0)
plt.xscale("log")
plt.yscale("log")
plt.plot(k_arr, pk_arr, label="linear mPk")
plt.plot(k_arr, tree_arr, label="linear/tree")
plt.plot(k_arr, tot_arr, label="total/full")
plt.legend()
plt.savefig("plots/check_lin_nonlin_SInu_PT.png")
plt.show()


