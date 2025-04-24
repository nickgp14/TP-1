import re
bdEstudiantes = [[("Juan","Pérez","Mora"), True, "2021021234", "jperez1234@estudiantec.cr", (85,47,70,65.7,65.7)]]

def registrarEstudiante(bdEstudiantes):
    """
    -Funcionamiento: Solicitar al usuario los datos del estudiante a registrar y validar con expresiones regulares
    -Entradas
    genero: Género del estudiante 1(para femenino) y 2(para masculino), ingresado por el usuario.
    nombre: Nombre del estudiante, ingresado por el usuario.
    apellido1: Primer apellido del estudiante, ingresado por el usuario.
    apellido2:Segundo apellido del estudiante, ingresado por el usuario.
    carne: Número de carné del estudiante, ingresado por el usuario.
    correo:Correo institucional del estudiante, ingresado por el usuario.
    -Salidas
    genero:
    nombre:Nombre del estudiante con la primera letra en mayúscula.
    apellido1: Primer apellido del estudiante con la primera letra en mayúscula.
    carne:Carné del estudiante ya validado en el formato correcto.
    correo:Correo del estudiante ya validado en el formato correcto.
    """
    while True:
        nombre=input("Ingrese nombre: ").strip().capitalize() #Se utiliza strip como medida preventiva para evitar errores por espacios vacíos.
        if re.match("[A-za-zÁÉÍÓÚáéíóúñÑ']+",nombre):
            break #Si el nombre tiene el formato adecuado, se rompe y solicita el siguiente dato
        else:
            print("Solo letras y apóstrofe permitido.")
    while True:
        apellido1=input("Ingrese su primer apellido: ").strip().capitalize()
        if re.match("[A-za-zÁÉÍÓÚáéíóúñÑ']+",apellido1):
            break
        else:
            print("Solo letras y apóstrofe permitido.")
    while True:
        apellido2=input("Ingrese su segundo apellido: ").strip().capitalize()
        if re.match("[A-za-zÁÉÍÓÚáéíóúñÑ']+",apellido2):
            break
        else:
            print("Solo letras y apóstrofe permitido.")
    nombreCompleto= nombre, apellido1,apellido2
    genero=input("¿Cuál es su género?\n1.Femenino.\n2.Masculino.\nIngrese según corresponda: ")
    while genero!="1" and genero!="2":
        print("Género no válido, ingrese 1 o 2.")
        genero=input("¿Cuál es su género?\n1.Femenino.\n2.Masculino.\nIngrese según corresponda: ")
    genero=validarGeneroAux(genero)
    while True:
        carne=input("Ingrese el carné(sin espacios, ni guiones): ")
        if re.match ("\d{10}",carne):
            #carne= formatocarne()  #Llamar a función ya creada que valida carné
            if existenciaCarne(bdEstudiantes,carne):
                print("Este carné ya existe, ingrese uno diferente.")
            else:
                break
        else:
            print("El carné debe ser de 10 dígitos positivos.Ejemplo: 2025042345")
    while True:
        correo=input("Ingrese correo: ").strip().lower()
        if re.match("[a-z]+\\d{4}\@estudiantec\\.cr",correo):
            #correo=Validarcorreo #reciclar función que ya verifica si el formato del correo es el requerido
            if existenciaCorreo(bdEstudiantes,correo):
                print("Este correo ya existe, ingrese uno diferente.")
            else:
                break
        else:
            print("El formato de correo no es válido,ingrese nuevamente uno válido.\nEjemplo: jmartinez1234@estudiantec.cr")

    while True:
        try:
            nota1=float(input("Ingrese la nota de la primera evaluación: "))
            nota1Temporal=validarNota1(nota1)
            if nota1Temporal==True:
                break
        except ValueError:
            print ("Debe ingresar un valor numérico.")
    while True:
        try:
            nota2=float(input("Ingrese la nota de la segunda evaluación: "))
            nota2Temporal=validarNota2(nota2)
            if nota2Temporal==True:
                break
        except ValueError:
            print("Debe ingresar un valor numérico.")
    while True:
        try:
            nota3=float(input("Ingrese la nota de la tercera evaluación: "))
            nota3Temporal=validarNota3(nota3)
            if nota3Temporal==True:
                break
        except ValueError:
            print("Debe ingresar un valor numérico.")
    #notas=#funcion que calcula nota final(debería devolver tupla)
    nuevoEstudiante=[nombreCompleto,carne,correo,notas] #Falta true o False
    bdEstudiantes.append(nuevoEstudiante)#bdEstudiante es la lista que tiene todas las listas
    return "¡Estudiante registrado exitosamente!"#nombre,apellido1,apellido2,genero,carne,correo
def validarGeneroAux(genero):
    """
    -Funcionamiento: Validar si es 1 a género se le asigna Femenino, si es 2 se le asigna Masculino.
    -Entradas
        genero: 1 o 2 según lo que ingreso el usuario.
    -Salidas
        genero: Femenino o masculino en función del 1 o 2 que había ingresado el usuario.
    """
    if genero=="1":
        genero="Femenino"
    else:
        genero=="2"
        genero="Masculino"
    return genero
def existenciaCarne(bdEstudiantes,carne):
    """
    Funcionamiento: Verificar si el carné generado existe ya dentro de la base de datos o no.
    -Entradas
    bdEstudiantes: Lista con las listas de cada estudiante.
    carne: Carné generado automáticamente.
    -Salidas
    True o False: Retorna True si el carné ya existe y False si es un carné único.
    """
    for estudiante in bdEstudiantes:
        if estudiante[2]==carne:
            return True
    return False
def existenciaCorreo(bdEstudiantes,correo):
     """
    Funcionamiento: Verificar si el correo generado existe ya dentro de la base de datos o no.
    -Entradas
    bdEstudiantes: Lista con las listas de cada estudiante.
    correo: Correo generado automáticamente.
    -Salidas
    True o False: Retorna True si el correo ya existe y False si es un carné único.
    """
    for estudiante in bdEstudiantes:
        if estudiante[3]==correo:
            return True
    return False
def validarNota1(nota1):
    if nota1>=0:
        return True
    else:
        print("La nota debe ser mayor o igual a 0.")
        return False
def validarNota2(nota2):
    if nota2>=0:
        return True
    else:
        print("La nota debe ser mayor o igual a 0.")
        return False
def validarNota3(nota3):
    if nota3>=0:
        return True
    else:
        print("La nota debe ser mayor o igual a 0.")
        return False
#Programa principal
print (registrarEstudiante(bdEstudiantes))
