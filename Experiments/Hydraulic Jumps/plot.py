import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.special import iv, kn

rc('text.latex',preamble='\\usepackage{libertine}\n\\usepackage[libertine]{newtxmath}')
rc('font',**{'family':'serif','serif':['Linux Libertine O']}, size=18)
rc('text', usetex=True)

t, Q, d = np.loadtxt('data.txt', unpack=True)
r = d/2

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1,1,1)

ax.plot(Q, r, ".", color="black")
ax.set_xlabel(r"$Q$ (cm$^3$/s)")
ax.set_ylabel(r"$r$ (cm)")
ax.set_xlim(10, 95)
ax.set_ylim(1.3, 6.9)

Q = np.linspace(1, 100, 100)
r = np.power(Q, 2/3)
ax.plot(Q, 0.34 * r, "-", color="red")

plt.savefig('fig.pdf', bbox_inches='tight')
