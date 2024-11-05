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
    #se eliminan valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
#ordenar la lista
vals.sort()

if len(vals)% !=0:
    k= len(vals)//2
    mediana= vals[k]            
else: 
    k= len(vals)//2 
    mediana= (vals[k-1]+ vals[k])
return mediana

def moda(vals):
	"""
	calcula la moda de una lista conteniendo una
	variable categoriva nominal
	Parametros
	-----------
	vals: list
	lista de categotias
	Retorna
	-------
	moda: str
		la moda de la muestra
	"""
#encontrar el conjunto de elementos unicos
  categorias=[]
  for v in vals:
	if v not in categorias:
	    categorias.append(v)
	#obtener el numero de cuentas en la muestra
	#para cada una de las categorias
  for c in categorias:
	n=0
	for val in vals:
	    if val==c:
		n=n+1
	cuentas.append(n)

#guess and check
 i_max=0
 val_max=cuentas[0]
  for i in range(1,len(cuentas)):
     if cuentas[i]> val_max:
	i_max=i
	val_max=cuentas[i]
#retorno la moda
  moda= categorias[i_max]



