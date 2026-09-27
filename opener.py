import numpy as np
import matplotlib.pyplot as plt

grads = np.load('5. veloc and grads - grid - iso/gradients-grid-iso-2M-t33.npy')

def S_3S_1(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    grads=grads.reshape(-1,3,3)
    for j in range(grads.shape[0]):
         
        A_i=grads[j]
        G_i=A_i@A_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0:
            minor_product=minor_3**0.5/minor_1**1.5
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def S_1S_3S_2(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    grads=grads.reshape(-1,3,3)
    for j in range(grads.shape[0]):
         
        A_i=grads[j]
        G_i=A_i@A_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0:
            minor_product=minor_1**0.5*minor_3**0.5/minor_2
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def S_1S_1(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    grads=grads.reshape(-1,3,3)
    for j in range(grads.shape[0]):
         
        A_i=grads[j]
        G_i=A_i@A_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0:
            minor_product=minor_2**0.5/minor_1
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def S_3S_1S_2(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    grads=grads.reshape(-1,3,3)
    for j in range(grads.shape[0]):
         
        A_i=grads[j]
        G_i=A_i@A_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0:
            minor_product=minor_1**(-1)*minor_3*minor_2**(-1)
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def S_3S_2(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    grads=grads.reshape(-1,3,3)
    for j in range(grads.shape[0]):
         
        A_i=grads[j]
        G_i=A_i@A_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0:
            minor_product=minor_3/minor_2**1.5
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

