from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Presente(models.Model):
    presente = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return str(self.presente)

class Convite(models.Model):
    title = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True)
    versicle = models.TextField(blank=True)
    refletion = models.TextField(blank=True)
    palavra_noivo = models.TextField(blank=True)
    palavra_noiva = models.TextField(blank=True)
    agradecimento = models.TextField(blank=True)
    noivo = models.CharField(max_length=50, blank=True)
    noiva = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return (self.title)
    
class Imagen(models.Model):
    pagina_login = models.ImageField(null=True, blank=True, upload_to="images/")
    pagina_inicial = models.ImageField(null=True, blank=True, upload_to="images/")
    pagina_perfil = models.ImageField(null=True, blank=True, upload_to="images/")
    noivos = models.ImageField(null=True, blank=True, upload_to="images/")
    pagina_confirm_1 = models.ImageField(null=True, blank=True, upload_to="images/")
    pagina_confirm_2 = models.ImageField(null=True, blank=True, upload_to="images/")
    pagina_confirm_3 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return ("Images do site")

class Convidado(models.Model):
    confirmar = models.BooleanField(default=False)
    acompanhante_1 = models.CharField(max_length=50, blank=True)
    acompanhante_2 = models.CharField(max_length=50, blank=True)
    acompanhante_3 = models.CharField(max_length=50, blank=True)
    presente = models.ForeignKey(Presente, on_delete=models.SET_NULL, null=True, blank=True)
    convidado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return (str(self.convidado))