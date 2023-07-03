import os
import imageio
nombre_imagen = ["team-pic1.png", "team-pic2.png"] # Almacenamos las rutas de los archivos
imagen = [ ] # Para almacenar nuestras imagenes
for nombre_imagenes in nombre_imagen:
    imagen.append(imageio.imread(nombre_imagenes)) # Biblioteca imageio y metodo imread(). El metodo carga una imagen basada en la ruta de archivos asique ahora la lista vacia ya tiene todas las imagenes.
imageio.mimsave("team-dos.gif", imagen, duration = 5.5) #EL metodo mimsave convierte las imagenes en un gif
"""
Team.gif es el nombre del archivo nuevo
imagen la lista de datos de imagenes
duration es el numero de segundos
"""

