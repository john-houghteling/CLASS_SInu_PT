import matplotlib.pyplot as plt
import numpy as np

# set true to plot ratio of files
ratio = True

to_output = "../output/"

# add all files to be considered here, may make argv later, if using ratio, 1st will be the norm
filename = ["mless_LCDM_PT_km100_pk.dat", "mless_LCDM_NONPT_km100_pk.dat"]
names = ["LCDM, 2 massive nu, SInu_PT", "LCDM, 2 massive nu, SInu_PT, PT disabled"]
dat = []

# read files
for i in range(0, len(filename)):
    with open(to_output + filename[i], 'r') as f:
        dat.append(f.readlines())

# remove file headers
for i in range(0, 4):
    for j in range(0,len(dat)):
        dat[j].pop(0)

k_arr = np.ndarray((len(dat), len(dat[0])))
pk_arr = np.ndarray((len(dat), len(dat[0])))
index_array = []
for i in range(0, len(dat)):
    index_empty = 0
    for j in range(0,len(dat[i])):
        k = dat[i][j][7:25]
        pk = dat[i][j][32:50]
        if float(k) >= 1e-3:
            k_arr[i][j] = k
            pk_arr[i][j] = pk
        else: 
            index_empty += 1
    index_array.append(index_empty)

#for i in range(0, len(k_arr)):
#    print(index_array[1])
#    print(k_arr[2][index_array[2]])

        

#print(k_arr[1][0])
#print(pk_arr[1][0])
if ratio:
    for i in range(1, len(pk_arr)):
        pk_arr[i] = np.divide(pk_arr[i], pk_arr[0])
    pk_arr[0] = np.divide(pk_arr[0],pk_arr[0])
print(len(k_arr[1]))
print(len(pk_arr[1]))
print(len(k_arr[0]))
print(len(pk_arr[0]))

plt.title("$P_k$ ratio")
plt.xlabel("k [h/Mpc]")
plt.ylabel("$P_{k, i}/P_{k, LCDM}$")
plt.xlim(0.001, 10.0)
plt.xscale("log")
plt.yscale("log")
for i in range(0, len(k_arr)):
    plt.plot(k_arr[i][index_array[i]:], pk_arr[i][index_array[i]:], label = names[i])
plt.legend()
plt.savefig("plots/SInu-PT-PT_vs_nonPT.png")
plt.show()
