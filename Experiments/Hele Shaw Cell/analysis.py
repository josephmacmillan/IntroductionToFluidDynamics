import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.special import iv, kn

rc('text.latex',preamble='\\usepackage{libertine}\n\\usepackage[libertine]{newtxmath}')
rc('font',**{'family':'serif','serif':['Linux Libertine O']}, size=18)
rc('text', usetex=True)

t, r = np.loadtxt('data.txt', unpack=True)

v = np.zeros(len(t))
for i in range(len(t) - 1):
	v[i] = (r[i+1] - r[i]) / (t[i+1] - t[i])

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1,1,1)

ax.plot(t, r,  ".", color="black")
ax.set_xlabel(r"$t$ (s)")
ax.set_ylabel(r"$r$ (cm)")
#ax.set_xlim(10, 95)
#ax.set_ylim(1.3, 6.9)


plt.savefig('fig.pdf', bbox_inches='tight')
