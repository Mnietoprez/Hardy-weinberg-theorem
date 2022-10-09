import matplotlib.pyplot as plt
import numpy as np
import random as rd

def init():
    continua = True
    while continua:
        AA = float(input("introduce pobabilidad inicial de AA (2 decimales)"))
        Aa = float(input("introduce pobabilidad inicial de Aa (2 decimales)"))
        aa= float(input("introduce pobabilidad inicial de aa (2 decimales)"))
        if(AA+Aa+aa == 1):
            continua = False
        else:
            print("AA + Aa + aa no suman 1")
    return AA, Aa, aa

n = int(input("introduce la cantidad de generaciones"))
muestra = int(input("introduce la muestra (>=100 y par)"))

AA, Aa, aa = init()

fAA=[muestra*AA]
fAa=[muestra*Aa]
faa=[muestra*aa]

def detectatipo(a):
    if (a<=100*AA):
        return 0
    elif (a>=100*AA and a <= 100*(AA + Aa)):
        return 1
    else:
        return 2
    
def reproducir(lista):
    if (lista[0]==0 and lista[1]==0):
        return 0
        
    elif (lista[0]==0 and lista[1]==1):
        if((rd.randint(0,9))>=5):
            return 0
        else: 
            return 1
        
    elif (lista[0]==0 and lista[1]==2):
        return 1
        
    elif (lista[0]==1 and lista[1]==0):
        if((rd.randint(0,9))>=5):
            return 0
        else: 
            return 1
    
    elif (lista[0]==1 and lista[1]==1):
        num = (rd.randint(0,11))
        if (num < 3):
            return 0
        elif (num>=3 and num<=8): 
            return 1
        else:
            return 2
    
        
    elif (lista[0]==1 and lista[1]==2):
        if((rd.randint(0,9))>=5):
            return 1
        else: 
            return 2
        
    elif (lista[0]==2 and lista[1]==0):
        return 1
        
    elif (lista[0]==2 and lista[1]==1):
        if((rd.randint(0,9))>=5):
            return 2
        else: 
            return 1
        
    else:
        return 2
    
for i in range(1,n):
    for j in range (int(muestra/2)):
        num1 = rd.randint(0,100)
        num2 = rd.randint(0,100)
        tipos= [detectatipo(num1), detectatipo(num2)]
        #cada pareja tiene 2 hijitos para mantener la especie
        r1 = reproducir(tipos)
        r2 = reproducir(tipos)
        AAcont=0
        Aacont=0
        aacont=0
        if(r1==1):
            Aacont +=1
        if(r1==2):
            aacont +=1
        if(r1==0):
            AAcont +=1
        if(r2==0):
            AAcont +=1
        if(r2==1):
            Aacont +=1
        if(r2==2):
            aacont +=1
    fAA.append(AAcont)
    fAa.append(Aacont)
    faa.append(aacont)
    
t = np.linspace(0,n,n)

plt.plot(t,fAA)
plt.plot(t,fAa)
plt.plot(t,faa)