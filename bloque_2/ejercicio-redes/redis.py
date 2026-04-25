
##Respuestas 2.1 
#Los contenedores pueden comunicarse usando el nombre del contenedor como dirección (por ejemplo "servidor"), gracias a que Docker provee resolución DNS interna dentro de la red.

#Respuesta 2.2
#Los datos persisten mientras el contenedor de Redis esté en ejecución. Sin embargo, si el contenedor de Redis se elimina o reinicia, los datos se pierden, 
# ya que no se configuró persistencia mediante volúmenes.