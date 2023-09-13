#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario o 
#Vamos a colocar diferentes metodos para poder realizar actividades simples o secuenciales
#del mismo modo permitira realizar salidas de informacion sujetas a condiciones logicas

print("-------------------------inicio del programa-------------------------------------")

Edad1 = int(input("Porfavor ingresar edad :  ")) 

if Edad1 < 18:
    print ("Eres menor de edad ")
else:
    print ("Eres mayor de edad   ")


print ("-------------------------------------------- Modulo de seguridad---------------------------------------------------------------------")

# Si el usuario es mayor de edad, se le pedirá ingresar una contraseña
# lo que hice fue que no pidiera contraseña a menores de edad porque ellos suponiendo un caso hipotetico 
# no tendrian acceso a el correo y solo se les pedidiria una frase
if Edad1 >= 18:
    print("Su contraseña fue enviada exitosamente a su correo")
    claveMayorEdad = "contraseñ0"
    password = input("Ingrese la contraseña que fue enviada a su correo: ")

    if claveMayorEdad == password.lower():
        print("Contraseña correcta")
        print("Bienvenido de nuevo")
    else:
        print("Contraseña incorrecta")
        print("Revise su contraseña e inténtelo de nuevo")
else:
    print("No se requiere contraseña para menores de edad")



print ("----------------------------------------------modulo 3 de interaccion---------------------------------------------- ") 

print ("Escriba una frase o palabra para seguir adelante en la autenticacion ")

frase = input ("introducir una frase  ")

#Si se desea remplazar la contraseña solicita al usuario escribir en diferentes letras o numeros la nueva contraseña o simplemente solicite un parametro de validacion 

if frase.lower() == "cambiar contraseña":
    nueva_contraseña = input("Introduzca la nueva contraseña: ")
    print("Contraseña actualizada con éxito")
else:
    print("No se realizó ningún cambio en la contraseña")

print("Ha completado los 3 módulos de autenticación. Gracias por su tiempo")
