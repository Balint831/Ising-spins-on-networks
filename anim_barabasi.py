from simulate_barabasi import *
from matplotlib import animation
import matplotlib.pyplot as plt

G = linPrefNet(100)

ising_net = IsingNet(G,-1)


ising_net.oneStep()
fig, ax = plt.subplots(figsize=[8,8])
ani = animation.FuncAnimation(fig, ising_net.anim, interval = 1, fargs = [ax], repeat = False)
#ani.save('animation_1.gif', writer='imagemagick')
plt.show()