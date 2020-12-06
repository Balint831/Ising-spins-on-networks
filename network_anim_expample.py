import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

colorDict = {-1: "red", 1: "blue"}
beta_j = 0.08

G = nx.fast_gnp_random_graph(30, 0.2)
spins = np.random.choice([-1,1], len(G.nodes))
pos = nx.spring_layout(G)
colorMap = [colorDict[element] for element in spins]

def anim(i):
    ax.clear()
    toFlip = np.random.choice( np.arange(len(G.nodes)) )
    neighbours = list(G.adj[ toFlip ])

    DEnergy = 2 * spins[toFlip] * ( spins[neighbours].sum() )

    if DEnergy < 0:
        spins[toFlip] *= -1
    elif DEnergy == 0:
        spins[toFlip] *= np.random.choice([-1,1])
    elif DEnergy > 0:
        spins[toFlip] *= np.random.choice([-1,1], p = [ np.exp(-beta_j  * DEnergy), 1 - np.exp(-beta_j  * DEnergy) ])

    colorMap = [colorDict[element] for element in spins]
    nx.draw(G, pos = pos, node_color=colorMap, ax = ax, alpha = 0.5)


fig, ax = plt.subplots(figsize=[6,4])
ani = animation.FuncAnimation(fig, anim, frames=10)
plt.show()