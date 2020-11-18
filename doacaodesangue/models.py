from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=50)
    RG = models.IntegerField()
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
    tipo_Sanguíneo = models.CharField(max_length=3, choices=tipo_Sanguíneo, default="")

    gênero = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'O', u'Outros'),
    )
    gênero = models.CharField(max_length=2, choices=gênero, default="")

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    CRM = models.IntegerField()
    especialidade = (
        (u'1', u'Hematologista'),
        (u'2', u'Enfermeira(o)'),
        (u'3', u'Outro'),
    )
    especialidade = models.CharField(max_length=12, choices=especialidade, default="")

    def __str__(self):
        return self.nome