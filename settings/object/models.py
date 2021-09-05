from django.db import models

class ObjectOfBuilding(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название объекта капитального строительства')
    adress = models.CharField(max_length=500, verbose_name='Адрес объекта капитального строительства')
    zastroishik = models.ForeignKey('Zastroishik', verbose_name='Застройщик (технический заказчик, эксплуатирующая организация или региональный оператор)')
    podriadchik = models.ForeignKey('Podriadchik', verbose_name='Подрядчик, лицо, осуществляющее строительство')
    proektniy_institut = models.ForeignKey('ProektniyInstitut', verbose_name='Лицо, осуществляющее подготовку проектной документации')
    tech_nadzor = models.ForeignKey('TechNadzor', verbose_name='Лицо, выполнившее работы, подлежащие освидетельствованию')
    date_from = models.DateField(verbose_name='Дата, от')
    date_to = models.DateField(verbose_name='Дата, до')

    def __str__(self) -> str:
        return f'Объект {self.name} по адресу {self.adress}'

class Organisation(models.Model):
    name = models.CharField(max_length=500, verbose_name='Наименование организации')
    ogrn = models.CharField(max_length=30, verbose_name='')
    inn = models.CharField(max_length=30, verbose_name='')
    adress = models.CharField(max_length=255, verbose_name='')
    city = models.CharField(max_length=50, verbose_name='')
    phone = models.CharField(max_length=20, verbose_name='')
    is_need_sro = models.BooleanField(default=False ,verbose_name='')
    sro = models.ForeignKey('SRO', verbose_name='')

    class Meta:
        abstract=True


class Zastroishik(Organisation):
    pass


class Podriadchik(Organisation):
    pass


class ProektniyInstitut(Organisation):
    pass


class TechNadzor(Organisation):
    pass


class SRO(models.Model):
    name = models.CharField(max_length=500, verbose_name='Наименование СРО')
    ogrn_sro = models.CharField(max_length=30, verbose_name='ОГРН СРО')
    inn_sro = models.CharField(max_length=30, verbose_name='ИНН СРО')
    date_from = models.DateField(verbose_name='Дата, от')
    date_to = models.DateField(verbose_name='Дата, до')