import numpy as np
import matplotlib.pyplot as plt
from opener import S_2S_1
from givernylocal.turbulence_dataset import turb_dataset
from givernylocal.turbulence_toolkit import getData

auth_token = "edu.jhu.pha.turbulence.testing-201406"

dataset = turb_dataset(
    dataset_title="isotropic1024coarse",
    output_path="./giverny_output",
    auth_token=auth_token
)

eta = 0.00287
n = 100
dz = eta * n

N = 4000
x0 = 0.0
y0 = 0.0
t = 0.0

z = np.arange(N) * dz

points = np.column_stack([
    np.full(N, x0),
    np.full(N, y0),
    z
])

gradients = getData(
    dataset,
    "velocity",
    t,
    "none",
    "fd4lag4",
    "gradient",
    points
)

gradients = np.asarray(gradients)
gradients = np.squeeze(gradients)
gradients = gradients.reshape(N, 3, 3)

np.save("gradients_z_4000.npy", gradients)
np.save("z_4000.npy", z)

x, y = S_2S_1(gradients)

plt.plot(x, y)
plt.xlabel(f"шаг матрицы = {n}η")
plt.grid(True)
plt.axhline(y=1, color="green")
plt.show()