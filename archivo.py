

from numpy import loadtxt#para cargar y dividir el archivo de texto en un array utilizando el parámetro delimiter
lines = loadtxt("notas.txt", delimiter=",")#delimiter para separar campos

print("estos son los numeros de la lista",lines,"y el tipo de datos es ",type(lines))