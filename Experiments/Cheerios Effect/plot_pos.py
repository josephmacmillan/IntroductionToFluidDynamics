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

ax.plot(t, xa, ".", color="blue")
ax.plot(t, xb, ".", color="red")
ax.set_xlabel(r"$t$ (s)")
ax.set_ylabel(r"$x$ (mm)")
ax.set_xlim(-0.05, 0.8)
ax.set_ylim(-5.9, 5.2)

# do diff including y too
diff = xb - xa
#ax.plot(t, diff, ".", color='blue')

alpha = 0.00017
l0 = 12e-3
fit = np.sqrt(l0**2 - alpha * t)
#ax.plot(t, fit, "-", color='green')

Lc = 2.71e-3 # m
l0 = 10.4e-3
l = l0
ell = []
ell.append(l)
time = 0.0
tt = []
tt.append(time)
dt = 0.001
beta = 0.18
while time < t[-1]:
	dl = -beta * kn(1, l/Lc) * dt
	l += dl
	ell.append(l)
	time += dt
	tt.append(time)
	
#ax.plot(tt, ell, "-", color='orange')
	

plt.savefig('fig_pos.pdf', bbox_inches='tight')
