import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time

N = 100
betaJ = 0.8
spins = np.random.choice([-1,1], size=[N,N])

def calcEnergy():
    '''
    choose a spin to flip, and calculate the change in energy accordingly
    '''
    global x,y #!!!
    x,y = np.random.choice(np.arange(N), size=2)

    #find it's neighbours, apply periodic boundary conditions
    xLeft = N-1 if x==0 else -1
    xRight = -(N-1) if x==N-1 else 1
    yAbove = N-1 if y==0 else -1
    yBelow = -(N-1) if y==N-1 else 1

    kernel_x = np.array([       0, 
                        xLeft,     xRight,
                                0,      ])
                        
    kernel_y = np.array([       yAbove,
                            0,              0,
                                yBelow,     ])

    neighbours = spins[x+kernel_x, y+kernel_y]

    #calculate Delta E energy
    dEnergy = 2* spins[x,y] * sum(neighbours)

    return dEnergy

def makeStep(dEnergy):
    '''
    make a step based on energy
    '''
    
    if dEnergy <= 0:
        spins[x,y] *= -1 #certrainly flip a spin

    else:
        spins[x,y] *= np.random.choice([-1,1] , 
                    p= [np.exp(-betaJ * dEnergy) , 1 - np.exp(-betaJ * dEnergy)]) #flip a spin with exp(-beta * dEnergy) chance


def anim_2dIsing(i):
    ax.clear()
    dE = calcEnergy()
    makeStep(dE)
    plt.imshow(spins, cmap="gray")

fig, ax = plt.subplots(figsize=[8,6])
plt.tight_layout()
ani = animation.FuncAnimation(fig, anim_2dIsing)
plt.show()