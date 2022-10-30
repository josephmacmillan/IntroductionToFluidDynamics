import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.special import iv, kn

rc('text.latex',preamble='\\usepackage{libertine}\n\\usepackage[libertine]{newtxmath}')
rc('font',**{'family':'serif','serif':['Linux Libertine O']}, size=18)
rc('text', usetex=True)

fps = 59.94

def plot_one(ax, frame):
	t = (frame - 7) / fps
	x, y = np.loadtxt(f'data_frame_{frame:02d}.txt', unpack=True)
	y += 1.1
	x += 0.86
	
	h0 = 4.0
	g = 980
	print(t)
	xx = np.linspace(-25, 25, 1000)
	h = h0 * np.ones(1000)
	c0 = np.sqrt(g * h0)
	h[xx>-c0*t] = 1/g * (2/3 * c0 - xx[xx>-c0*t]/3/t)**2
	h[xx>2*c0*t] = 0
	
	
	ax.plot(x, y, "-", color="red", lw=1)
	ax.fill_between(xx, h, color="lightblue")
	

fig = plt.figure(figsize=(10, 6))

y1 = -1
y2 = 5
ax = fig.add_subplot(3,1,1)
ax.set_aspect('equal')
ax.set_ylim(y1, y2)

plot_one(ax, 14)

ax = fig.add_subplot(3,1,2)
ax.set_aspect('equal')
ax.set_ylabel("$h$ (cm)")
ax.set_ylim(y1, y2)
plot_one(ax, 28)
ax = fig.add_subplot(3,1,3)
ax.set_aspect('equal')
ax.set_xlabel("$x$ (cm)")
ax.set_ylim(y1, y2)
plot_one(ax, 42)

plt.savefig('fig.pdf', bbox_inches='tight')
