import os
import numpy as np
from givernylocal.turbulence_dataset import turb_dataset
from givernylocal.turbulence_toolkit import getData


auth_token = "edu.jhu.pha.turbulence.testing-201406"

eta = 0.00287
t = 0.0
N = 100000
steps = [0.5, 1, 2, 5, 10, 20, 50]

step_length = 4000

output_directory = "./grads_data"                    #куда сохраняем
os.makedirs(output_directory, exist_ok=True)         #если папки нет, она сама создастся, если есть, то все норм продолжаем


dataset = turb_dataset(
    dataset_title="isotropic1024coarse",             #к какому датасету обращаемся
    output_path=output_directory,                    #куда сохраняем
    auth_token=auth_token                            #наш тестовый токен на запрос
)


rng = np.random.default_rng(37)  
x = rng.uniform(0, 2 * np.pi, N)
y = rng.uniform(0, 2 * np.pi, N)
np.save(f"{output_directory}/x.npy", x)
np.save(f"{output_directory}/y.npy", y)


def download_gradients(points):                             
    gradients_parts = []
    for start in range(0, len(points), step_length):        
        end = min(start + step_length, len(points))         
        series = points[start:end]                           
        print(f"{start}:{end} / {len(points)}")             

        g = getData(
            dataset,
            "velocity",
            t,
            "none",
            "fd4lag4",
            "gradient",
            series
        )
        g = np.asarray(g)
        g = np.squeeze(g)
        g = g.reshape(-1, 3, 3)
        gradients_parts.append(g)
    return np.concatenate(gradients_parts, axis=0)      #append только для numpy


all_points_list = []
all_gradients_list = []


for n in steps:
    z = n * eta
    points = np.column_stack([
        x,
        y,
        np.full(N, z)                #строчка заполненная значениями z 
    ])
    print()
    print(f"Layer {n} eta")
    print(f"z = {z}")

    gradients = download_gradients(points)

    step_name = str(n).replace(".", "_")                                        #здесь просто сохраняем в файлы
    np.save(f"{output_directory}/points_z_{step_name}eta.npy", points)
    np.save(f"{output_directory}/gradients_z_{step_name}eta.npy", gradients)
    all_points_list.append(points)
    all_gradients_list.append(gradients)

    print(f"gradients_z_{step_name}eta.npy", gradients.shape)

all_points = np.concatenate(all_points_list, axis=0)                #list --> numpy
all_gradients = np.concatenate(all_gradients_list, axis=0)  
all_gradients = all_gradients.reshape(len(steps), N, 3, 3)
all_gradients = all_gradients.transpose(1, 0, 2, 3)        

np.save(f"{output_directory}/all_points.npy", all_points)
np.save(f"{output_directory}/all_gradients.npy", all_gradients)

print("all good")
