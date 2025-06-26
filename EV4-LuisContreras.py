usuarios={}

def ingresarUsuario():
    nombre=input(" ingrese el nombre de usuario a registrar \n ")
    if nombre in usuarios:
        print(" error: el nombre ya existe!!")
        return
    sexo=input(" ingrese su sexo (F-M) \n ").upper()
    if sexo not in ["F","M"]:
        print(" solo se permiten letras  'F' o 'M' ")
        return
    contraseña=input(" ingrese  contraseña \n ")
    if not validar_Contraseña(contraseña):
        print("debe ser de minimo largo 8 caracteres")
        print("debe tener al menos un numero")
        print("debe tener al menos una letra ")
        print("no puede tener espacios en blanco")
        return
    usuarios[nombre]= {'sexo':sexo , 'contraseña':contraseña }
    print(" usuario ingresado exitosamente ")
    print("*"*100)

def validar_Contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if ' ' in contraseña:
        return False
    letra= any(c.isalpha() for c in contraseña)
    numero=any(c.isdigit() for c in contraseña)
    return letra and numero

def buscarUsuario():
    nombre=input(" ingrese nombre de usuario a buscar \n ")
    if nombre in usuarios:
        datos=usuarios[nombre]
        print(f"sexo:{datos['sexo']}")
        print(f"contraseña:{datos['contraseña']}")
        print("*"*100)
    else:
        print(" el usuario no se encuentra" )
        print("*"*100)

def eliminarUsuario():
    nombre=input(" ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print(" usuario eliminado" )
        print("*"*100)
    else:
        print(" no se pudo eliminar  usuario")
        print("*"*100)

try:
    while True:
        print("***** MENU PRINCIPAL *****")
        print("1- ingresar usuario")
        print("2- buscar usuario ")
        print("3- eliminar usuario")
        print("4- salir")
        opc=input(" ingrese una opcion (1-4): ")
        if opc=="1":
            ingresarUsuario ()
        elif opc=="2":
            buscarUsuario ()
        elif opc=="3":
            eliminarUsuario ()
        elif opc=="4":
            print(" programa terminado ")
            break
        else:
            print(" opcion invalida, selecione una opcion entre 1-4 :" )

except ValueError:
    print(" ingrese una opcion valida ")