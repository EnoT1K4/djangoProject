from django.db import models


class Article(models.Model):
    title = models.CharField('Naming', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateField('Date')

    def __str__(self):
        return self.title
