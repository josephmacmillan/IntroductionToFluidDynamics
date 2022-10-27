import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.special import iv, kn

rc('text.latex',preamble='\\usepackage{libertine}\n\\usepackage[libertine]{newtxmath}')
rc('font',**{'family':'serif','serif':['Linux Libertine O']}, size=18)
rc('text', usetex=True)

t, r, n = np.loadtxt('data_fingers.txt', unpack=True)


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1,1,1)

#ax.step(r, n,   color="black", where='post')
ax.plot(r, n, '.',   color="black")
ax.set_xlabel(r"$r$ (cm)")
ax.set_ylabel(r"$n$")
#ax.set_xlim(10, 95)
#ax.set_ylim(1.3, 6.9)


plt.savefig('fig2.pdf', bbox_inches='tight')
