# Vamos a crear un codigoque realice por pantalla un calculo de variables, que nos permita sumar 
# restar y hacer operaciones para mostrar al final un resltado de cada operacion y a su vez crear una tabla de 
# la verdad y cada una de las operaciones usando "boot" o usando and y or.""

print("Este programa no se puede hacer por chat gpt el que lo hago le bajo nota")

j = input ("dame un nunmero en la pantalla ")
u = input ("inserte un numero mayor al anterior ")


j = int(j)
u = int (u)

print (j+u)
print (j-u)
print (j*u)
print (j/u)
print (j%u)

print ("Tabla de la verdad todo lo relacionado con and o Y")
# Disyuncuion
print ((str(j==j)) + "and" + str (j==j) + "--->" + str (j==j))
print ((str(j==j)) + "and" + str (j==u) + "--->" + str (j==j))
print ((str(j==u)) + "and" + str (j==j) + "--->" + str (j==j))
print ((str(j==u)) + "and" + str (u==j) + "--->" + str (u==j))

print("--------------------------------")

# Conjuncion  

print ((str(j==j)) + "o" + str (j==j) + "--->" + str (j==j))
print ((str(j==j)) + "o" + str (j==u) + "--->" + str (j==u))
print ((str(u==j)) + "o" + str (j==j) + "--->" + str (j==u))
print ((str(j==u)) + "o" + str (u==j) + "--->" + str (u==j))





