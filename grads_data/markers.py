import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------

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

def S_2S_1(grads:np.ndarray) -> list:
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

#------------------------------------------------------------------------------------------------------

def S_2S_1_layers(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    for j in range(grads.shape[0]):
        for i in range(grads.shape[1]):
            A_i=grads[j, i]
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

#------------------------------------------------------------------------------------------------------

def S_2S_1_double(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        B_i=grads[j, 6]
        G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
        matrix=G_i
        minor_1=matrix[0,0]
        minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
        minor_3=np.linalg.det(matrix)
        if minor_1>0 and minor_2>0:
            minor_product=minor_2**0.5/minor_1
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def G_22m_23_double(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        B_i=grads[j, 1]
        G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
        matrix=G_i
        G_22=matrix[1,1]
        M_23=matrix[1,1]*matrix[2,2]-matrix[2,1]*matrix[1,2]
        if G_22>0 and M_23>0:
            minor_product=G_22**(-1)*M_23**(0.5)
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

def G_33m_13_double(grads:np.ndarray) -> list:
    x=[]
    y=[]
    sum=0
    count=0
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        B_i=grads[j, 6]
        G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
        matrix=G_i
        G_33=matrix[2,2]
        M_13=matrix[0,0]*matrix[2,2]-matrix[2,0]*matrix[0,2]
        if G_33>0 and M_13>0:
            minor_product=G_33**(-1)*M_13**(0.5)
            sum+=minor_product
            count+=1
            y.append(sum/count)
            x.append(count)
    return x, y

#------------------------------------------------------------------------------------------------------

def S_2S_1_4(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        for i in range(1, 7):  
            A_i=grads[j, i]
            G_i=A_i@A_i@A_i.transpose()@A_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_2**0.5/minor_1
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

#------------------------------------------------------------------------------------------------------

def S_2S_1_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_2**0.5/minor_1
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def S_3S_1_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_3**0.5/minor_1**1.5
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

    

def S_1S_3S_2_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_1**0.5*minor_3**0.5/minor_2
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def S_3S_1S_2_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_1**(-1)*minor_3*minor_2**(-1)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def S_3S_2_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_3/minor_2**1.5
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

#------------------------------------------------------------------------------------------------------

def G_22M_23_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            G_22=matrix[1,1]
            M_23=matrix[1,1]*matrix[2,2]-matrix[2,1]*matrix[1,2]
            if G_22>0 and M_23>0:
                minor_product=G_22**(-1)*M_23**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_33M_13_DOUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@A_i.transpose()@B_i.transpose()
            matrix=G_i
            G_33=matrix[2,2]
            M_13=matrix[0,0]*matrix[2,2]-matrix[2,0]*matrix[0,2]
            if G_33>0 and M_13>0:
                minor_product=G_33**(-1)*M_13**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

#------------------------------------------------------------------------------------------------------


def S_2S_1_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            minor_1=matrix[0,0]
            minor_2=matrix[0,0]*matrix[1,1]-matrix[0,1]*matrix[1,0]
            minor_3=np.linalg.det(matrix)
            if minor_1>0 and minor_2>0:
                minor_product=minor_2**0.5/minor_1
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_22M_23_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_22=matrix[1,1]
            M_23=matrix[1,1]*matrix[2,2]-matrix[2,1]*matrix[1,2]
            if G_22>0 and M_23>0:
                minor_product=G_22**(-1)*M_23**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_33M_13_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_33=matrix[2,2]
            M_13=matrix[0,0]*matrix[2,2]-matrix[2,0]*matrix[0,2]
            if G_33>0 and M_13>0:
                minor_product=G_33**(-1)*M_13**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_11M_13_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_11=matrix[0,0]
            M_13=matrix[0,0]*matrix[2,2]-matrix[2,0]*matrix[0,2]
            if G_11>0 and M_13>0:
                minor_product=G_11**(-1)*M_13**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_33M_23_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_33=matrix[2,2]
            M_23=matrix[1,1]*matrix[2,2]-matrix[2,1]*matrix[1,2]
            if G_33>0 and M_23>0:
                minor_product=G_33**(-1)*M_23**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_11M_12_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_11=matrix[0,0]
            M_12=matrix[0,0]*matrix[1,1]-matrix[1,0]*matrix[0,1]
            if G_11>0 and M_12>0:
                minor_product=G_11**(-1)*M_12**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

def G_22M_12_DOUBLE_TROUBLE(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_22=matrix[1,1]
            M_12=matrix[0,0]*matrix[1,1]-matrix[1,0]*matrix[0,1]
            if G_22>0 and M_12>0:
                minor_product=G_22**(-1)*M_12**(0.5)
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y

#------------------------------------------------------------------------------------------------------

def G_33M_13_DOUBLE_LN(grads:np.ndarray) -> list:
    x=[[] for _ in range(6)]
    y=[[] for _ in range(6)]
    sum=[0.0] *6
    count=[0] *6
    for j in range(grads.shape[0]):
        A_i=grads[j, 0]
        for i in range(1, 7):  
            B_i=grads[j, i]
            G_i=A_i@B_i@B_i.transpose()@A_i.transpose()
            matrix=G_i
            G_33=matrix[2,2]
            M_13=matrix[0,0]*matrix[2,2]-matrix[2,0]*matrix[0,2]
            if G_33>0 and M_13>0:
                minor_product=np.log(G_33**(-1)*M_13**(0.5))
                sum[i-1]+=minor_product
                count[i-1]+=1
                y[i-1].append(sum[i-1]/count[i-1])
                x[i-1].append(count[i-1])
    return x, y