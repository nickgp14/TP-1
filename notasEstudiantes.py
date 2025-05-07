#Elaborado por: Nicole Gamboa Padilla y Piero Cunio López
#Fecha de creación: 30/04/2025 11:09 p.m.
#Última modificación: 02/05/2025 10:00 p.m.
#Versión de Python: 3.13.2
import re
from funciones import *
import smtplib
import os
from email.message import EmailMessage
inicial=2020
final=2025
sedes=["Cartago","San Carlos","San José"]
bdEstudiantes=[[("Juan","Pérez","Mora"),True,2022021234,"nicoleiveth2017@gmail.com", (20,60,56,65.7, 65)],[("Ana", "Gómez", "López"), False, 2023031234, "nicolegamboa1406@gmail.com", (90, 85, 95, 90.0, 80)],
    [("Laura", "Díaz", "Soto"), False, 202104235, "n.gamboa.1@estudiantec.cr", (80, 75, 70, 75.0, 90)]]
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
    if registrarEstudiante(nombreCompleto,genero,carne,correo,notas,bdEstudiantes):
         print("\n¡Estudiante registrado exitosamente!\n")
    else:
        print("Ha ocurrido un error al registrar al estudiante, intente nuevamente.")
    return ""
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
        nombre=input("Ingrese el nombre: ").strip().title() #Se utiliza strip para evitar espacios vacíos al final o principio.
        print(nombre)
        if validarNombreCompleto(nombre):
            break #Si el nombre tiene el formato adecuado, se rompe y solicita el siguiente dato
        else: 
            print("Por favor, ingrese únicamente letras, espacios(nombres compuestos) y apóstrofes.")
    while True:
        apellido1=input("Ingrese su primer apellido: ").strip().title()
        if validarNombreCompleto(apellido1):
            break
        else:
            print("Por favor, ingrese únicamente letras, espacios(nombres compuestos) y apóstrofes.")
    while True:
        apellido2=input("Ingrese su segundo apellido: ").strip().title()
        if validarNombreCompleto(apellido2):
            break
        else:
            print("Por favor, ingrese únicamente letras, espacios(nombres compuestos) y apóstrofes.")
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
        if re.match (r"\d{10}",carne):
            #carne= formatocarne()  #Llamar a función ya creada que valida carné
            if existenciaCarne(bdEstudiantes,carne):
                print("Este carné ya existe, ingrese uno diferente.")
            else:
                break
        else:
            print("El carné debe ser de 10 dígitos positivos.Ejemplo: 2025042345")
    while True:
        correo=input("Ingrese correo: ").strip().lower()
        if re.match(r"^[a-z]+\d{4}\@estudiantec\.cr$",correo):
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
       
def reportePorGeneroAux(bdEstudiantes):
    """
    Funcionamiento: Genera una base de datos para femenino y otra para masculino y las ordena de mayor a menor en promedios.
    -Entradas:
    bdEstudiantes(lista de listas): Base de datos general con todos los estudiantes.
    -Salidas:
    bdFemenino(lista de listas): Base de datos con las mujeres ordenado de mayor a menor por promedio.
    bdMasculino(lista de listas): Base de datos con hombres ordenado de mayor a menor por promedio.
    """
    bdFemenino=[]
    bdMasculino=[]
    for estudiante in bdEstudiantes:
        if estudiante[1]==True:
            bdMasculino.append(estudiante)
        else:
            bdFemenino.append(estudiante)
    #Se reescribe cada base de datos para que contenga los estudiantes en el formato requerido para el reporte.
    bdMasculino=decodificarEstudiantes(bdMasculino)
    bdFemenino=decodificarEstudiantes(bdFemenino)
    #Se ordenan las listas de estudiantes por promedio de mayor a menor.
    bdMasculino=sorted(bdMasculino, key=lambda estudiante:estudiante[0],reverse=True)
    bdFemenino=sorted(bdFemenino, key=lambda estudiante:estudiante[0],reverse=True)
    return bdMasculino,bdFemenino
def reportePorGeneroES():
    """
    Funcionamiento: Hace las llamadas a la funcion principal con bdMasculino y bdFemenino, para crear los docx con el reporte
    -Entradas:
    (No recibe parámetros)
    -Salidas:
    mensaje1(str): Indica al usuario que los reportes se generaron con éxito.
    """
    bdMasculino,bdFemenino=reportePorGeneroAux(bdEstudiantes)
    reportePorGenero("masculino.docx",bdMasculino)
    reportePorGenero("femenino.docx",bdFemenino)
    print("\nLos reportes han sido generados con éxito.")
    return""
#Estadística por generación
def estadisticaPorGeneracionAux(inicial,final):
    """
    Funcionamiento: Llama a la función que calcula el rango de años y retorna a la función de proceso
    -Entradas:
    inicial(int): Año inicial que ingresó el usuario.
    final(int): Año final que ingresó el usuario
    -Salidas:
    estadisticaPorGeneracion(función): Retorna a la función del proceso principal
    """
    annos=calcularAnnos(inicial,final)
    return estadisticaPorGeneracion(bdEstudiantes,annos)
def estadisticaPorGeneracionES():
    """
    Funcionamiento: Llama a la función Auxiliar que llamó a la de proceso e imprime la tabla con los encabezados correctos.
    -Entradas:
    (No recibe parámetros)
    -Salidas:
    tabla(lista de listas):Imprime las filas de la tabla y los encabezados
    """
    tabla=estadisticaPorGeneracionAux(inicial,final)
    print(f"\nAño\tAprobados\tReposición\tReprobados\tTotal")
    for fila in tabla:
     print(f"{fila[0]}\t{fila[1]}\t\t{fila[2]}\t\t{fila[3]}\t\t{fila[4]}")
    print("\n")
#Reporte por Sede con Buen Rendimiento
def reportePorSedeBuenRendimientoAux(bdEstudiantes):
     """
     Funcionamiento: Crea una lista con los mejores rendimientos de la base de datos de estudiantes.
     -Entradas:
     bdEstudiantes(lista de listas): La base de datos dinámica con todos los estudiantes
     -Salidas:
     mejores(lista de listas): Los estudiantes con notas de 70 o más en las 3 evaluaciones
     """
     mejores=[]
     for estudiante in bdEstudiantes:
        notas=estudiante[-1][:3]
        if notas[0]>=70 and notas[1]>=70 and notas[2]>=70:
            mejores.append(estudiante)
     return mejores 
def reportePorSedeBuenRendimientoES():
    """
    Funcionamiento: Muestra el submenú al usuario con las sedes disponibles y le solicita la elección, además, imprime resultados
    -Entradas:
    eleccion(str):Se solicita al usuario un valor numérico según las opciones presentadas.
    -Salidas:
    reporte(str): Se imprime al usuario el reporte de los estudiantes con mejor rendimiento de la sede que solicitó.
    """
    if not bdEstudiantes:
        print("\nNo hay estudiantes registrados en la base de datos, necesita al menos uno para realizar el reporte.")
        return ""  
    i=1
    for sede in sedes:
        print(f"{i}.{sede}")
        i+=1
    while True:
        try:
            eleccion=input("Ingrese el número de la sede que desea vizualizar: ")
            if int(eleccion)>=1 and int(eleccion)<=(i-1):
                break
            else:
                print("Opción inválida, ingrese un número de las opciones.")
        except ValueError:
            print("Debe ingresar un valor númerico válido.")    
    mejores=reportePorSedeBuenRendimientoAux(bdEstudiantes)
    reporte=reportePorSedeBuenRendimiento(mejores,eleccion)
   
    print(reporte)
    return ""
def enviarCorreosReposicionAux(est):
    remitente=os.getenv("correo")
    clave=os.getenv("clave")
    if not remitente:
        print("Variable de entorno correo no configurada.")
        return False
    elif not clave:
        print ("Variable de entorno clave no configurada.")
        return False
    asunto="Notificación de reposición"
    nombre=" ".join(est[0])
    cuerpo=f"""
Estimado/a: {nombre}

Se le hace saber que usted deberá realizar el examen de reposición debido a que su nota es de {est[4][-1]}.
Para ello deberá presentarse el día y la hora indicados a continuación.
Fecha: 15/05/2025
Hora: 1:00 p.m
Lugar: Edificio D3

A partir del momento en que recibió este correo, usted cuenta con 3 días hábiles para confirmar su asistencia, 
de lo contrario perderá su derecho al examen de reposición.

Atentamente,
Coordinación Académica.
"""
        
    mensaje=EmailMessage()
    mensaje["From"]=remitente
    mensaje["To"]= est[3]
    mensaje["Subject"]=asunto
    mensaje.set_content(cuerpo)
    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente, clave)
        smtp.send_message(mensaje)
        smtp.quit()
        print(f"Correo enviado a {est[3]}")
        return True
    except Exception as e:
        print(f"Error al enviar correo a {est[3]}: {e}, verifique su conexión a internet")
        return False
def enviarCorreosReposicionES():
    estudiantesReposicion=enviarCorreosReposicion(bdEstudiantes)
    for est in estudiantesReposicion:
        enviarCorreosReposicionAux(est)
    print("\nCorreos enviados con éxito")
    return  True

def traerVariables():
    try:
        extraer=open(".env","r")
        for linea in extraer:
            if "=" in linea: #Si existe un = en la línea
                nombre,valor=linea.strip().split("=",1) #Tome la línea y divida del = hacia atras como nombre y hacia adelante como valor
                os.environ[nombre] = valor
    except FileNotFoundError:
        print("Archivo no encontrado")

def validarNombreCompleto(texto):
    if re.match(r"^[A-za-zÁÉÍÓÚáéíóúñÑ']+$",texto):
        return True
    else:
        return False

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
def menu():
    """
    -Funcionamiento: Muestra el menú de opciones al usuario y llama a la función correspondiente según la opción elegida.
    -Entradas
    opcion(int): Opción elegida por el usuario.
    -Salidas
    menu(función): Llama a la función menú para mostrar nuevamente las opciones al usuario.
    """
    print("\n")
    print("1. Crear Base de Datos dinámica")
    print("2. Registrar un estudiante")
    print("3. Generar reporte HTML y .csv")
    print("4. Respaldar en XML")
    print("5. Reporte por género(.docx)")
    print("6. Gestionar curva")
    print("7. Envio de correos reposición")
    print("8. Aplazados en almenos 2 exámenes(.pdf)")
    print("9. Estadística por generación")
    print("10.Reporte por sede con buen rendimiento")
    print("11.Salir")
    while True:
        try:
            opcion=int(input("Ingrese la opción requerida: "))
            if opcion>=1 and opcion<=11:
                break
            else:
                print("Por favor, ingrese una de las opciones presentadas.")
        except ValueError:
            print("Debe ingresar un valor numérico válido")
    if opcion==1:
        print("En proceso")
    elif opcion==2:
        registrarEstudiantesES()
    elif opcion==3:
        print("En proceso")
    elif opcion==4:
        print("En proceso")
    elif opcion==5:
        reportePorGeneroES()
    elif opcion==6:
        print("En proceso")
    elif opcion==7:
            traerVariables()
            enviarCorreosReposicionES()
    elif opcion==8:
        print("En proceso")
    elif opcion==9:
        estadisticaPorGeneracionES()
    elif opcion==10:
        reportePorSedeBuenRendimientoES()
    else:
        return
    menu()
#Programa principal
menu()
