from django.db import models
# Класс филиала----------------------------------------------------------------
class Filial(models.Model):
    name = models.CharField('Название филиала',max_length=50)
    external_id = models.IntegerField('Внешний ID')

    def __str__(self):
        return self.name
# Класс региона---------------------------------------------------------------
class Region(models.Model):
    name = models.CharField('Название региона',max_length=50)
    # zone_broadcast = models.IntegerField('Внешний ID', max_length=10)
    filial = models.ForeignKey(Filial, verbose_name='name', on_delete=models.CASCADE, null=False, default=None)

    def __str__(self):
        return  self.name

# Класс Цеха---------------------------------------------------------------

class Cekh(models.Model):
    name = models.CharField('Название Цеха',max_length=50)
    region = models.ForeignKey(Region, verbose_name='name', on_delete=models.CASCADE, null=False, default=None)

    def __str__(self):
            return self.name