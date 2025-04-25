#Elaborado por:
#
import re
from funciones import *
bdEstudiantes=[]
def menu():
    print("1. Crear Base de Datos dinámica")
    print("2. Registrar un estudiante")
    print("3. Generar reporte HTML y .csv")
    print("4. Respaldar en XML")
    print("5. Reporte por género(.docx)")
    print("6. Gestionar curva")
    print("7. Envio de correos")
    print("8. Aplazados en almenos 2 exámenes(.pdf)")
    print("9. Estadística por generación")
    print("10.Reporte por sede con buen rendimiento")
    print("11.Salir")
    opcion=int(input("Ingrese la opción requerida: "))
    if opcion>=1 and opcion<=11:
        if opcion==1:
            print("En proceso")
        elif opcion==2:
            registrarEstudiantesES()
        elif opcion==3:
            print("En proceso")
        elif opcion==4:
            print("En proceso")
        elif opcion==5:
            print("En proceso")
        elif opcion==6:
            print("En proceso")
        elif opcion==7:
            print("En proceso")
        elif opcion==8:
            print("En proceso")
        elif opcion==9:
            print("En proceso")
        elif opcion==10:
            reporteBuenRendimientoES()
        else:
            return
    else:
        print("Opción inválida, indique una de las anteriores.")
    menu()
def registrarEstudiantesAux(nombre,apellido1,apellido2,genero,carne,correo,nota1,nota2,nota3):
    """
    Funcionamiento: Toma los datos proporcionados y los coloca en una tupla para mayor facilidad de manejo.
    -Entradas
    nombre(str): Nombre del estudiante, ya validado.
    apellido1(str):Primer apellido del estudiante, ya validado.
    apellido2(str):Segundo apellido del estudiante, ya validado.
    genero(booleano): True si es masculino y False si es femenino.
    carne(str): Número de carné del estudiante, ya validado.
    correo(str): Correo institucional del estudiante, ya validado.
    nota1(float): Nota de la primera evaluación, ya validada.
    nota2(float):Nota de la segunda evaluación, ya validada.
    nota3(float): Nota de la segunda evaluación, ya validada.
    -Salidas
    registrarEstudiante(función): Retorna a la función principal una tupla de datos para registrar al estudiante en la base de datos.
    """
    nombreCompleto=(nombre,apellido1,apellido2)
    notas=(nota1,nota2,nota3)#sacarPromedio(nota1,nota2,nota3)
    return registrarEstudiante(nombreCompleto,genero,carne,correo,notas,bdEstudiantes)
def registrarEstudiantesES():
    """
    -Funcionamiento: Solicitar al usuario los datos del estudiante a registrar y validar con expresiones regulares
    -Entradas
    nombre(str): Nombre del estudiante, ingresado por el usuario.
    apellido1(str): Primer apellido del estudiante, ingresado por el usuario.
    apellido2(str):Segundo apellido del estudiante, ingresado por el usuario.
    genero(int): Género del estudiante 1(para masculino) y 2(para femenino), ingresado por el usuario.
    carne(str): Número de carné del estudiante, ingresado por el usuario.
    correo(str):Correo institucional del estudiante, ingresado por el usuario.
    -Salidas
    nombre(str):Nombre del estudiante con la primera letra en mayúscula.
    apellido1(str): Primer apellido del estudiante con la primera letra en mayúscula.
    apellido2(str): Segundo apellido del estudiante con la primera letra en mayúscula.
    genero(booleano):El género como True para masculino y False para femenino.
    carne(str):Carné del estudiante ya validado en el formato correcto.
    correo(str):Correo del estudiante ya validado en el formato correcto.
    """
    while True:
        nombre=input("Ingrese el nombre: ").strip().capitalize() #Se utiliza strip como medida preventiva para evitar errores por espacios vacíos.
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
    while True:
        try:
            genero=int(input("¿Cuál es su género?\n1.Masculino.\n2.Femenino.\nIngrese según corresponda: "))
            if validarGenero(genero):
                if genero==1:
                    genero=True
                else:
                    genero=False
                break
            else:
                print("El número no es válido.")
        except ValueError:
            print("Debe ingresar un valor numérico")
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
    return registrarEstudiantesAux(nombre,apellido1,apellido2,genero,carne,correo,nota1,nota2,nota3)

def validarGenero(genero):
    """
    -Funcionamiento: Valida si el número es ino de los permitidos.
    -Entradas
    genero(int): 1 o 2 según lo que ingreso el usuario.
    -Salidas
    True o False(booleano): Devuelve False si el número no es 1 o 2 y True si el número es 1 o 2.
    """
    if genero!=1 and genero!=2:
        return False
    else:
        return True
def existenciaCarne(bdEstudiantes,carne):
    """
    Funcionamiento: Verificar si el carné ingresado existe ya dentro de la base de datos o no.
    -Entradas
    bdEstudiantes(lista): Lista con las listas de cada estudiante.
    carne(str): Carné ingresado por el usuario.
    -Salidas
    True o False(booleano): Retorna True si el carné ya existe y False si es un carné único.
    """
    for estudiante in bdEstudiantes:
        if estudiante[2]==carne:
            return True
    return False
def existenciaCorreo(bdEstudiantes,correo):
    """
    Funcionamiento: Verificar si el correo ingresado existe ya dentro de la base de datos o no.
    -Entradas
    bdEstudiantes(lista): Lista con las listas de cada estudiante.
    carne(str): Carné ingresado por el usuario.
    -Salidas
    True o False(booleano): Retorna True si el carné ya existe y False si es un carné único.
    """
    for estudiante in bdEstudiantes:
        if estudiante[3]==correo:
            return True
    return False
def validarNota1(nota1):
    """
    -Funcionamiento: Verificar si la nota de la primera evaluación está dentro de los valores permitidos.
    -Entradas
    nota1(float): Nota de la primera evaluación.
    -Salidas
    True o False(booleano): Devuelve True si la nota está entre 0 y 100 , y False si es negativa o superior a 100.
    mensaje(str):Indica al usuario que la nota debe estar entre 0 y 100.
    """
    if nota1>=0 and nota1<=100:
        return True
    else:
        print("La nota debe ser mayor o igual a 0 y menor o igual que 100.")
        return False
def validarNota2(nota2):
    """
    -Funcionamiento: Verificar si la nota de la primera evaluación está dentro de los valores permitidos.
    -Entradas
    nota2(float): Nota de la primera evaluación.
    -Salidas
    True o False(booleano): Devuelve True si la nota está entre 0 y 100 , y False si es negativa o superior a 100.
    mensaje(str): Indica al usuario que la nota debe estar entre 0 y 100.
    """
    if nota2>=0 and nota2<=100:
        return True
    else:
        print("La nota debe ser mayor o igual a 0 y menor o igual que 100.")
        return False
def validarNota3(nota3):
    """
    -Funcionamiento: Verificar si la nota de la primera evaluación está dentro de los valores permitidos.
    -Entradas
    nota3(float): Nota de la primera evaluación.
    -Salidas
    True o False(booleano): Devuelve True si la nota está entre 0 y 100 , y False si es negativa o superior a 100.
    mensaje(str): Indica al usuario que la nota debe estar entre 0 y 100.
    """
    if nota3>=0 and nota3<=100:
        return True
    else:
        print("La nota debe ser mayor o igual a 0 y menor o igual que 100.")
        return False
#Programa principal
menu()
