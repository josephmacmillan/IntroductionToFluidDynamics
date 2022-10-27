import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.special import iv, kn

rc('text.latex',preamble='\\usepackage{libertine}\n\\usepackage[libertine]{newtxmath}')
rc('font',**{'family':'serif','serif':['Linux Libertine O']}, size=18)
rc('text', usetex=True)

t, xa, ya, xb, yb = np.loadtxt('data.txt', unpack=True)
xa = xa*1000
xb = xb*1000
ya = ya*1000
yb = yb*1000

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1,1,1)

ax.set_xlabel(r"$t$ (s)")
ax.set_ylabel(r"$\ell$ (mm)")
ax.set_xlim(-0.05, 0.8)
ax.set_ylim(3.5, 10.6)

# do diff including y too
diff = np.sqrt((xb - xa)**2 + (yb - ya)**2)
ax.plot(t, diff, ".", color='black')

alpha = 100
l0 = 10.4
fit = np.sqrt(l0**2 - alpha * t)
ax.plot(t, fit, "-", color='red')

Lc = 2.71 # mm
l0 = 10.4
l = l0
ell = []
ell.append(l)
time = 0.0
tt = []
tt.append(time)
dt = 0.001
beta = 32.6
while time < t[-1]:
	dl = (-beta * kn(1, l/Lc)) * dt
	l += dl
	ell.append(l)
	time += dt
	tt.append(time)
	
#ax.plot(tt, ell, "-", color='orange')
	

plt.savefig('fig_diff.pdf', bbox_inches='tight')