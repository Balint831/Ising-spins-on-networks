from simulate_2dGrid import *

grid = Ising2D(150, -1)

fig, ax = plt.subplots(figsize=[6,4])
ani = animation.FuncAnimation(fig, anim_grid, interval = 1, fargs = [grid, ax], repeat = False)
plt.show()