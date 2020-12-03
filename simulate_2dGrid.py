import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import random

class Ising2D:
    def __init__(self, N, BETA):
        self.N = N
        self.beta  = BETA
        self.spins = np.random.choice([-1,1], size = [N,N])
    
    def oneStep(self):
        '''for x in range(self.N):
            for y in range(self.N):'''
        for i in range(self.N*10):
            x,y = random.choices(range(self.N),k=2)
            self.updateSpins(x, y)

    def calcEnergy(self, x, y):
        
        xLeft = self.N-1 if x==0 else -1
        xRight = -(self.N-1) if x==self.N-1 else 1
        yAbove = self.N-1 if y==0 else -1
        yBelow = -(self.N-1) if y==self.N-1 else 1

        kernel_x = np.array([xLeft, 0, xRight,
                             xLeft,    xRight,
                             xLeft, 0, xRight])
                            
        kernel_y = np.array([yAbove, yAbove, yAbove,
                                  0,              0,
                             yBelow, yBelow, yBelow])

        neighbours = self.spins[ x + kernel_x, y + kernel_y]
        dEnergy = 2 * self.spins[x, y] * sum(neighbours)
        return dEnergy

    def updateSpins(self, x, y):
        dEnergy = self.calcEnergy(x, y)
        if dEnergy <= 0:
            self.spins[x,y] *= -1 #certrainly flip a spin

        elif random.random() > math.exp(-self.beta * dEnergy):
            self.spins[x,y] *= -1

def anim(i):
    ax.clear()
    a.oneStep()
    plt.imshow(a.spins, cmap="gray")
