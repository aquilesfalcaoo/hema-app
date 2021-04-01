from django.db import models

<<<<<<< HEAD
class Doador(models.Model):
    nome = models.CharField(max_length=50)
    RG = models.IntegerField()
=======

class Doador(models.Model):
    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=14, default="")
>>>>>>> 7208dc4 (added jquery function)
    tipo_Sanguíneo = (
        ('1', u'AB+'),
        ('2', u'AB-'),
        ('3', u'A+'),
        ('4', u'A-'),
        ('5', u'B+'),
        ('6', u'B-'),
        ('7', u'O+'),
        ('8', u'O-'),
    )
<<<<<<< HEAD
    tipo_Sanguíneo = models.CharField(max_length=3, choices=tipo_Sanguíneo, default="")

    gênero = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'O', u'Outros'),
    )
    gênero = models.CharField(max_length=2, choices=gênero, default="")
=======
    tipo_Sanguíneo = models.CharField(
        max_length=3, choices=tipo_Sanguíneo, default="")

    sexo = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    sexo = models.CharField(max_length=2, choices=sexo, default="")
>>>>>>> 7208dc4 (added jquery function)

    def __str__(self):
        return self.nome

<<<<<<< HEAD
=======

>>>>>>> 7208dc4 (added jquery function)
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    CRM = models.IntegerField()
    especialidade = (
        (u'1', u'Hematologista'),
        (u'2', u'Enfermeira(o)'),
        (u'3', u'Outro'),
    )
<<<<<<< HEAD
    especialidade = models.CharField(max_length=12, choices=especialidade, default="")

    def __str__(self):
        return self.nome
=======
    especialidade = models.CharField(
        max_length=12, choices=especialidade, default="")

    def __str__(self):
        return self.nome
>>>>>>> 7208dc4 (added jquery function)
