import math 
def promedio(lista):
    """
    calcula el promedio de una lista.
    
    parametros:
    -------------
    lista: lista de variables aleatorias
    
    retorna:
    ------------
    promedio : float
    """
    
    vals= []
    for v in lista:
        if math.isfinite(v):
            vals.append(v)
        
    promedio=sum(vals)/len(vals)
    return promedio

def mediana(vals_in):
    """
    Calcula la mediana de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    mediana:float
        la mediana de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    
    #ordenar la lista
    vals.sort()
    if len(vals)%2!=0:
        k=len(vals)//2
        mediana=vals[k]
    else:
        k=len(vals)//2
        mediana=(vals[k-1]+vals[k])/2
    return mediana
def moda():
    for v in vals:
        if v not in categorias:
            categorias.append(v)
    for c in categorias:
        n=0
        for val in vals:
            if val ==c:
                n=n+1
        cuentas.append(n)
    i_max=0
    val_max= cuentas[0]
    for i in range(1,len(cuentas)):
        if cuentas[i]> val_max:
            i_max = i
            val_max=cuentas[i]
    modas=[]
    for i in range(len(cuentas)):
        if cuentas[i]= val_max:
            modas.append(categorias[i])
    
    moda= categorias[i_max]
    return moda
