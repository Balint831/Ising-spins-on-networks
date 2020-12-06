from simulate_2dGrid import *

grid = Ising2D(150, -1, betaFix=False)

fig, ax = plt.subplots(figsize=[6,4])
ani = animation.FuncAnimation(fig, grid.anim, interval = 1, fargs = [ax], repeat = False, save_count = 300)
ani.save('2d_grid.gif', writer='ffmpeg')
#plt.show()