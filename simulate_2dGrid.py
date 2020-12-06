import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import random

class Ising2D:
    def __init__(self, N, beta, betaFix = True):
        self.N = N
        self.beta  = beta
        if betaFix == False:
            self.beta_list = np.linspace(2,-2,50)
        self.spins = np.random.choice([-1,1], size = [N,N])
    
    def oneStep(self):
        for i in range(self.N*30):
            x,y = random.choices(range(self.N),k=2)
            self.updateSpins(x, y)
        self.m = np.mean(self.spins).round(3)

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

    def anim(self, i, ax):
        ax.clear()
        try:
            self.beta = self.beta_list[i//3 % len(self.beta_list)]
        except AttributeError:
            pass 
        
        self.oneStep()
        plt.imshow(self.spins, cmap="gray")
        plt.title(f"m = {self.m}\n beta = {self.beta.round(3)}",size=14)

'''def anim_grid(i, grid, ax):
    ax.clear()
    grid.oneStep()
    plt.imshow(grid.spins, cmap="gray")
    plt.title(f"m = {grid.m}",size=18)'''
