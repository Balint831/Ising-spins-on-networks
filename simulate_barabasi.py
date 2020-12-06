import numpy as np
import random
import math
import networkx as nx

class IsingNet:
    def __init__(self, G, beta, betaFix = True):
        self.G = G
        self.N = len(G.nodes)
        self.beta = beta
        if betaFix == False:
            self.beta_list = np.linspace(2,-2,100)

        self.spins = np.random.choice([-1,1], size = self.N)

        self.pos = nx.spring_layout(G)
        self.colorDict = {-1: "red", 1: "blue"}

    def oneStep(self):
        toFlip = random.choice(range(self.N))
        dEnergy = self.calcEnergy(toFlip)

        if dEnergy <= 0:
            self.spins[toFlip] *= -1 #certrainly flip a spin

        elif random.random() > math.exp(-self.beta * dEnergy):
            self.spins[toFlip] *= -1
    

    def calcEnergy(self, toFlip):
        neighbours = list(self.G.adj[ toFlip ])
        dEnergy = 2 * self.spins[toFlip] * ( self.spins[neighbours].sum() )
        return dEnergy


    def anim(self, i, ax):
        ax.clear()
        try:
            self.beta = self.beta_list[i % len(self.beta_list)]
        except AttributeError:
            pass 
        self.oneStep()
        colorMap = [self.colorDict[element] for element in self.spins]
        nx.draw(self.G, pos = self.pos, node_color=colorMap, ax = ax, alpha = 0.5)


def linPrefNet(N):
    G = nx.fast_gnp_random_graph(10, 0.2)

    for i in range(N-10):
        degDist = [ G.degree[x] for x in G.nodes]
        q = random.choices(list(G.nodes), weights = degDist)
        G.add_edge(max(G.nodes)+1,q[0])

    return G

def powPrefNet(N, power):
    G = nx.fast_gnp_random_graph(10, 0.2)

    for i in range(N-10):
        degDist = np.array([ G.degree[x] for x in G.nodes])
        q = np.random.choice(list(G.nodes), p = degDist**power / sum(degDist**power))
        G.add_edge(max(G.nodes)+1,q[0])

    return G