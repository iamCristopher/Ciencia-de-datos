
from estadistica import moda,promedio,mediana,rango,varianza,desviacion_estandar
import numpy as np
archivo=open("bsc_sel.dat","r")
archivo.readline()
HR = []
HD=[]
Vmag=[]
BV=[]
SpType=[]
for lin in archivo:
    HR.append(int(lin.split()[0]))
    HD.append(int(lin.split()[1]))
    if lin.split()[2]=='""':
        Vmag.append(np.nan)
    else:
        Vmag.append(float(lin.split()[2]))
    if lin.split()[3]=='""':
        BV.append(np.nan)
    else:
        BV.append(float(lin.split()[3]))
    if lin.split()[4]=='""':
        SpType.append(np.nan)
    else:
        SpType.append(str(lin.split()[4]))

archivo.close()
print("La moda es: ",moda(Vmag))
print("La promedio es: ",promedio(Vmag))
print("La mediana es: ",mediana(Vmag))
print("La rango es: ",rango(Vmag))
print("La varianza es: ",varianza(Vmag))
print("La desviacion estandar es: ",desviacion_estandar(Vmag))
