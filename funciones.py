
def registrarEstudiante(nombreCompleto,genero,carne,correo,notas,bdEstudiantes):
     """
     Funcionamiento: Crea el formato para el nuevo estudiante y lo registra en la base de datos.
     -Entradas
     nombreCompleto: Tupla con el nombre, primer apellido y segundo apellido del estudiante.
     genero: True si es masculino y False si es femenino.
     carne: Número de carné del estudiante.
     correo: Correo institucional del estudiante.
     notas: Tupla con las notas del estudiante
     bdEstudiantes: Lista que tiene los demás estudiantes.
     -Salidas
     mensaje: Le informa al usuario si el estudiante fué registrado con éxito.
     """
     nuevoEstudiante=[nombreCompleto,genero,carne,correo,notas]
     bdEstudiantes.append(nuevoEstudiante)
     return True
def reportePorGenero(nombreDeArchivo,baseDeDatos):
    """
    Funcionamiento: Se encarga de escribir en un archivo cada estudiante con el formato requerido, junto a la cantidad de estudiantes
    -Entradas:
    nombreDeArchivo(str):El nombre del archivo a buscar o crear
    baseDeDatos(lista de listas):La base de datos sea de mujeres o de hombres
    -Salidas:
    archivo(docx): Genera el archivo que se le ha pedido con los datos específicados.
    """
    abrir=open(nombreDeArchivo,"w",encoding="utf-8")
    abrir.write("Notas         Nombre Completo   Carné    Correo Institucional\n----------------------------------------------------------------\n")
    for estudiante in baseDeDatos:
        linea=str(estudiante[0])+","+str(estudiante[1])+","+str(estudiante[2])+","+str(estudiante[3])+","+str(estudiante[4])+" "+str(estudiante[5])+" "+str(estudiante[6])+","+str(estudiante[7])+","+str(estudiante[8])+"\n"
        abrir.write(linea) 
    abrir.write("Porcentajes de evaluaciones:(Faltan porcentajes)\n")  
    abrir.write("La cantidad de estudiantes es: "+ str(len(baseDeDatos))) 
    abrir.close()
    return""
def decodificarEstudiantes(bdEstudiantes):
    """
    Funcionamiento: Crea un nuevo conjunto de datos para cada estudiante, con el formato requerido para el reporte indicado en el enunciado.
    -Entradas:
    estudiante(lista):Lista de estudiante con sus datos.
    -Salidas:
    nuevaBD(lista):Lista con los datos de cada estudiante en el formato requerido.
    """
    nuevaBD=[]
    for estudiante in bdEstudiantes:
        nombre=estudiante[0][0]
        apellido1=estudiante[0][1]
        apellido2=estudiante[0][2]
        carne=estudiante[2]
        correo=estudiante[3]
        nota1=estudiante[4][0]
        nota2=estudiante[4][1]
        nota3=estudiante[4][2]
        promedio=estudiante[4][-1]
        nuevoEst=(promedio,nota1,nota2,nota3,nombre,apellido1,apellido2,carne,correo)
        nuevaBD.append(nuevoEst)
    return nuevaBD
def calcularAnnos(inicial,final):
    """
    Funcionamiento: Forma una lista con el rango de años entre inicial y final(dados por el usuario)
    -Entradas:
    inicial(int):El año inicial que ingresó el usuario.
    final(int):El año final que ingresó el usuario.
    -Salidas:
    annos(lista): Lista con el rango de años con cada año en str para facilidad de manipulación.
    """
    annos=[]
    for anno in range(inicial,final+1):
        annos.append(str(anno))
    return annos
def estadisticaPorGeneracion(bdEstudiantes,annos):
    """
    Funcionamiento: Se encarga de crear la tabla con la cantidad de aprobados, reposición y reprobados en cada fila y columna correspondiente
    -Entradas:
    bdEstudiantes(lista de listas):Contiene a los estudiantes de la base de datos
    annos(lista):Una lista con los años en el rango que ingreso el usuario, para las generaciones.
    -Salidas:
    tabla(lista de listas): La tabla con cantidad de aprobados, reposición y reprobados por generación y con los totales.
    """
    tabla=[]
    for anno in annos:
        tabla.append([anno,0,0,0,0,])
    tabla.append(["Total",0,0,0,0])
    for estudiante in bdEstudiantes:
        gen=str(estudiante[2])[0:4]
        for fila in tabla:
            if gen==fila[0]:
                promedio=estudiante[4][-1]
                if promedio>70:
                    estado=1
                elif promedio>60:
                    estado=2
                else:
                    estado=3
                fila[estado]+=1
                fila[4]+=1
    for i in range(1, len(tabla[-1])):  #Calcula entre cuantas columnas se debe mover(excluye la última)
        for fila in tabla[:-1]:  #
            tabla[-1][i] += fila[i]
    tabla[-1][-1]=" "
    return tabla
def reportePorSedeBuenRendimiento(mejores,eleccion):
    """
    Funcionamiento: Agrega a los que coincidan con la eleccion del usuario a los mejores por sede.
    -Entradas:
    mejores(lista de listas):Los estudiantes con notas de 70 o más en las 3 evaluaciones.
    eleccion(str): El número que ingresó el usuario.
    -Salidas:
    reporte(str): Los datos de los estudiantes formateados para mayor legibilidad.
    """
    mejoresSede=[]
    for estudiante in mejores: #Busca en cada estudiante de los mejores
           sedeE=str(estudiante[2])[4:6]    #Toma la sede del estudiante(del carné)
           if sedeE==("0"+eleccion):        #A la eleccion del usuario le coloca un 0 para que se pueda comparar correctamente
                mejoresSede.append(estudiante)
    if len(mejoresSede)==0:
        return f"No hay estudiantes con buen rendimiento en la sede {eleccion}"
    reporte=f"\nLos estudiantes con mejor rendimiento de la sede {eleccion} son:\n"
    i=1
    for estudiante in mejoresSede:
        nombre=estudiante[0]
        if estudiante[1]:
            genero="Masculino"
        else:
            genero="Femenino"
        carne=estudiante[2]
        correo=estudiante[3]
        notas=estudiante[4]
        reporte+=f"\n{i}.{nombre[0]} {nombre[1]} {nombre[2]},{genero},{carne},{correo},{notas}"
        i+=1
    return reporte
def enviarCorreosReposicion(bdEstudiantes):
    """
    Funcionamiento: Genera una base de datos con los estudiantes que deben hacer reposición
    -Entradas:
    bdEstudiantes(lista de listas): La base de datos madre donde estan todos los estudiantes
    -Salidas:
    bdEstudiantesReposicion(lista de listas): La base de datos solo con los estudiantes con la nota de acta igual o superior a 60 pero inferior a 70
    """
    bdEstudiantesReposicion=[]
    for estudiante in bdEstudiantes:
        promedio=estudiante[4][-1]
        if promedio<70 and promedio>=60:
            bdEstudiantesReposicion.append(estudiante)
    return bdEstudiantesReposicion


        
