from django.db import models


class Artefato(models.Model):
    descricao = models.TextField(
        blank=True, null=True, verbose_name='descrição')
    nome = models.CharField(max_length=70)
    situacao = models.CharField(max_length=25)
    data_entrega = models.DateField(verbose_name="data de entrega")

    def __str__(self):
        return self.nome
