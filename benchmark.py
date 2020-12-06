import numpy as np
import random
import matplotlib.pyplot as plt
import time
np_times = {}
stl_times = {}



for N in range(100,3000,100):
    w = random.choices(range(10), k = N)
    temp1 = []
    temp2 = []
    for _ in range(7):
        time1 = time.time()
        q = np.random.choice(w, p = [ x/sum(w) for x in w])
        temp1.append(time.time()-time1)
    for _ in range(7):
        time2 = time.time()
        qq = random.choices(w, weights = w)
        temp2.append(time.time()-time2)

    np_times [N]  = temp1
    stl_times [N]  = temp2  

plt.figure(figsize=[16,6])
plt.subplot(121)
plt.errorbar(np_times.keys(), np.array(list(np_times.values())).mean(axis=1), yerr = np.array(list(np_times.values())).std(axis=1), capsize=4, marker="s", ls = "", color ="red")
plt.title("Linear preferential network - initialization time",size=14)
plt.xlabel("N - number of nodes ", size=14)
plt.ylabel("t [s]",size=14)
plt.grid()
plt.subplot(122)
plt.errorbar(stl_times.keys(), np.array(list(stl_times.values())).mean(axis=1), yerr = np.array(list(stl_times.values())).std(axis=1), capsize=4, marker="s", ls = "", color ="red")
plt.title("Linear preferential network - initialization time",size=14)
plt.xlabel("N - number of nodes ", size=14)
plt.ylabel("t [s]",size=14)
plt.grid()

plt.show()