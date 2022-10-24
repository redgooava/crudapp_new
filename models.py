from django.db import models
from django.contrib.auth.models import User


class Datatable(models.Model):
    cell_1 = models.CharField(max_length=255, blank=True, null=True)  # Подчинённость
    cell_2 = models.CharField(max_length=255, blank=True, null=True)  # Наименование ВЛО
    # Субъект Российской Федерации
    cell_3 = models.CharField(max_length=255, blank=True, null=True)
    cell_4 = models.CharField(max_length=255, blank=True, null=True)  # Дислокация ВЛО
    # Всего коек в ВМО
    # - развёрнуто
    cell_5 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_6 = models.PositiveIntegerField(blank=True, null=True)  # из них под covid-19
    # - занято
    cell_7 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_8 = models.PositiveIntegerField(blank=True, null=True)  # из них с пациентами с covid-19
    # - в том числе:
    # - - инфекционные
    # - - - развёрнуто
    cell_9 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_10 = models.PositiveIntegerField(blank=True, null=True)  # из них под covid-19
    # - - - занято
    cell_11 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_12 = models.PositiveIntegerField(blank=True, null=True)  # из них пациентами с covid-19
    # - - реанимационные
    # - - - развёрнуто
    cell_13 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_14 = models.PositiveIntegerField(blank=True, null=True)  # из них под covid-19
    # - - - занято
    cell_15 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_16 = models.PositiveIntegerField(blank=True, null=True)  # из них пациентами с covid-19
    # - - прочие
    # - - - развёрнуто
    cell_17 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_18 = models.PositiveIntegerField(blank=True, null=True)  # из них под covid-19
    # - - - занято
    cell_19 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_20 = models.PositiveIntegerField(blank=True, null=True)  # из них пациентами с covid-19
    # Количество пациентов с коронавирусной инфекцией
    # - состояло по состоянию на 9:00 предыдущих суток
    cell_21 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_22 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - поступило в течение суток
    cell_23 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_24 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - выбыло с определившимся исходом в течение суток
    cell_25 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_26 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - переведено в другие медицинские организации в течение суток
    cell_27 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_28 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - состоит на 9:00 текущих суток
    # - - Всего
    cell_29 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_30 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - - подтверждённых лабораторно
    cell_31 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_32 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # - - с пневмонией
    cell_33 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_34 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # в тяжёлом состоянии
    cell_35 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_36 = models.PositiveIntegerField(blank=True, null=True)  # в т.ч. в/с
    # Количество военнослужащих в зоне ответственности ВМО
    # - с коронавирусной инфекцией
    cell_37 = models.PositiveIntegerField(blank=True, null=True)  # всего
    # - - в медицинских учреждениях государственной и муниципальной систем здравоохранения
    cell_38 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_39 = models.PositiveIntegerField(blank=True, null=True)  # с пневмонией
    cell_40 = models.PositiveIntegerField(blank=True, null=True)  # в тяжёлом состоянии

    cell_41 = models.PositiveIntegerField(blank=True, null=True)  # на дому

    # - контактных по коронавирусной инфекции
    cell_42 = models.PositiveIntegerField(blank=True, null=True)  # всего
    cell_43 = models.PositiveIntegerField(blank=True, null=True)  # в обсерваторе
    cell_44 = models.PositiveIntegerField(blank=True, null=True)  # на дому

    cell_45 = models.CharField(max_length=255, blank=True, null=True)  # госпиталь
    cell_46 = models.DateField(blank=True, null=True)  # дата
    cell_47 = models.ForeignKey(User, on_delete=models.CASCADE)  # внешний id
    cell_48 = models.CharField(max_length=255, blank=True, null=True)  # округ

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s ' \
               '%s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.cell_1, self.cell_2, self.cell_3, self.cell_4,
                                                           self.cell_5, self.cell_6, self.cell_7, self.cell_8,
                                                           self.cell_9, self.cell_10, self.cell_11, self.cell_12,
                                                           self.cell_13, self.cell_14, self.cell_15, self.cell_16,
                                                           self.cell_17, self.cell_18, self.cell_19, self.cell_20,
                                                           self.cell_21, self.cell_22, self.cell_23, self.cell_24,
                                                           self.cell_25, self.cell_26, self.cell_27, self.cell_28,
                                                           self.cell_29, self.cell_30, self.cell_31, self.cell_32,
                                                           self.cell_33, self.cell_34, self.cell_35, self.cell_36,
                                                           self.cell_37, self.cell_38, self.cell_39, self.cell_40,
                                                           self.cell_41, self.cell_42, self.cell_43, self.cell_44,
                                                           self.cell_45, self.cell_46, self.cell_47, self.cell_48)  # для видимости
        # значений (cell_?) из админ-части


class ExcelFile(models.Model):
    files = models.FileField(upload_to='excel')
