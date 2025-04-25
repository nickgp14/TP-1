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
     return"¡Estudiante registrado exitosamente!"
    
