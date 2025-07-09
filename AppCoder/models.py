from django.db import models

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    año_lanzamiento = models.IntegerField()

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    plataforma = models.ForeignKey(Consola, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    videojuego = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"Reseña de {self.videojuego} por {self.autor}"

class Truco(models.Model):
    videojuego = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"Truco para {self.videojuego}"