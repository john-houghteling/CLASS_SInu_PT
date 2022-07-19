import matplotlib.pyplot as plt
import numpy as np

# set true to plot ratio of files
ratio = True

#speed of sound?? cs with same value as in notebook
#cs = 1 #(Mpc/h)^2
#h = 0.6732

# add all files to be considered here, may make argv later, if using ratio, 1st will be the norm
filename = ["../output/2m_LCDM_PT_pk_nl_pt.dat", "../output/1c2m_1Geff6_PT_pk_nl_pt.dat"]
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
mless_k_arr = np.empty(len(dat[0]))
sinu_k_arr = np.empty(len(dat[1]))
mless_tree_arr = np.empty(len(dat[0]))
sinu_tree_arr = np.empty(len(dat[1]))
for i in range(0, len(dat[0])):     
    mless_k_arr[i] = dat[0][i][0]
    mless_tree_arr[i] = dat[0][i][9]
for i in range(0, len(dat[1])):
    sinu_k_arr[i] = dat[1][i][0]
    sinu_tree_arr[i] = dat[1][i][9]

# divide for ratio plot if needed
if ratio:
    sinu_tree_arr = np.divide(sinu_tree_arr, mless_tree_arr)
    mless_tree_arr = np.divide(mless_tree_arr, mless_tree_arr)

#print(tot_arr)
#print(tree_arr)
# plot and save
plt.title("$P_k$ ratio")
plt.xlabel("k [h/Mpc]")
plt.ylabel("$P_{k, i}/P_{k, LCDM}$")
plt.xlim(0.001, 1.)
#plt.ylim(0.9,2.0)
plt.xscale("log")
#plt.yscale("log")
plt.plot(mless_k_arr, mless_tree_arr, label="LCDM, 1 massless nu 2 massive, SInu_PT")
plt.plot(sinu_k_arr, sinu_tree_arr, label="SInu 1c2m Geff=10^-6")
plt.legend()
plt.savefig("plots/nonPT_mLCDM_vs_1c2mG6_1.png")
plt.show()


