from markers import *
import numpy as np
import matplotlib.pyplot as plt

steps = [0.5, 1, 2, 5, 10, 20, 50]

grads = np.load('/home/solnisko/Documents/Symmetry/grads_data/all_gradients.npy')


x, y = G_33M_13_DOUBLE_LN(grads)

for i in range(1, 7):
    plt.plot(x[i-1],y[i-1], label=f"{steps[i]-0.5}eta")

plt.grid(True)
plt.legend()
plt.ylim(0.9,1.2)
plt.axhline(y=1, color="green")
plt.savefig('G_33M_13_LN_A_i@B_i@B_i^t@A_i^t.png')
plt.show()