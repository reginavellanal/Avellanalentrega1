from django.db import models

class Products(models.Model): #estoy creando el primer modelo, despues puedo cambiar products por departamento o lo que se me ocurra
    name = models.CharField(max_length=100)
    distance = models.FloatField() #en vez de precio puede ser los kilometros que queda desde montevideo
    stock = models.BooleanField(default=True) #si hay panaderias adheridas o no

    def __str__(self):
        return self.name
#despues de crear el modelo tengo que correr en la terminal 'python manage.py makemigrations' para que cree la aplicación
#despues hacemos 'python manage.py migrate'

#class Categorie(models.Model):
    #name = models.CharField(max_length=50, unique=True) #unique true es que ninguna categoria puede repetir los nombres
#este es el modelo de las categorias el cual pienso agrupar los departamentos por zonas geograficas de uruguay
    #def __str__(self):
        #return self.name

class Panaderia(models.Model):
    name = models.CharField(max_length=100)
    horario = models.FloatField()
    stock = models.BooleanField(default=True)  #está abierta o no
    
    def __str__(self):
        return self.name