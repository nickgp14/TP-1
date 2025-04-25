def registrarEstudiante(nombreCompleto,genero,carne,correo,notas,bdEstudiantes):
     nuevoEstudiante=[nombreCompleto,genero,carne,correo,notas]
     bdEstudiantes.append(nuevoEstudiante)
     print (bdEstudiantes)
     return"Estudiante registrado exitosamente"
    
