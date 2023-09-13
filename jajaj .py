print("-------------------------inicio del programa-------------------------------------")

edad = int(input("Por favor, ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

print("-------------------------------------------- Módulo de seguridad ---------------------------------------------------------------------")

# Si el usuario es mayor de edad, se le pedirá ingresar una contraseña
if edad >= 18:
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

print("---------------------------------------------- Módulo 3 de interacción ----------------------------------------------")

print("Escriba una frase o palabra para continuar con la autenticación")
frase = input("Introduzca una frase: ")

# Si se desea reemplazar la contraseña, solicita al usuario escribir en diferentes letras o números la nueva contraseña o simplemente solicite un parámetro de validación

if frase.lower() == "cambiar contraseña":
    nueva_contraseña = input("Introduzca la nueva contraseña: ")
    print("Contraseña actualizada con éxito")
else:
    print("No se realizó ningún cambio en la contraseña")

print("Ha completado los 3 módulos de autenticación. Gracias por su tiempo")
