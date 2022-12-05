

from numpy import loadtxt#para cargar y dividir el archivo de texto en un array utilizando el parámetro delimiter
lines = loadtxt("notas.txt", delimiter=",")#delimiter para separar campos

#print("estos son los numeros de la lista",lines,"y el tipo de datos es ",type(lines))

#print("esto es un dato de tipo" ,type(lines)) 

lista =[]

lista2 =lines[0]

lista1 = lines[0]





for i in lista1: #accediendo a las posiciones 
    parceo = float(i)
    lista.append(parceo)

for i in lista2:
    parceo2 = float(i)
    lista.append(parceo2)


print(lista)



