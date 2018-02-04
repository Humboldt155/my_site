from django.db import models


class Department(models.Model):
    code = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["code"]
        verbose_name = "LMRussia отдел"
        verbose_name_plural = "LMRussia_1 отделы"

    def __str__(self):
        return str(self.code)


class DepartmentAdeo(models.Model):
    code = models.CharField(max_length=6, primary_key=True, unique=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["code"]
        verbose_name = "отдел Adeo"
        verbose_name_plural = "Adeo_1 отделы"

    def __str__(self):
        return self.code


class SubDepartmentAdeo(models.Model):
    code = models.CharField(max_length=12, primary_key=True, unique=True)
    name = models.CharField(max_length=60)
    department_adeo = models.ForeignKey(DepartmentAdeo, on_delete=models.PROTECT)

    class Meta:
        ordering = ["code"]
        verbose_name = "подотдел Adeo"
        verbose_name_plural = "Adeo_2 подотделы"

    def __str__(self):
        return self.code


class ModelGroupAdeo(models.Model):
    code = models.CharField(max_length=14, primary_key=True, unique=True)
    name = models.CharField(max_length=60)
    sub_department_adeo = models.ForeignKey(SubDepartmentAdeo, on_delete=models.PROTECT)

    class Meta:
        ordering = ["code"]
        verbose_name = "Adeo группа моделей"
        verbose_name_plural = "Adeo_3 группы моделей"

    def __str__(self):
        return self.code


# Model Adeo
class Model(models.Model):
    code = models.CharField(max_length=10, primary_key=True, unique=True)
    french_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    russian_name = models.CharField(max_length=200)
    model_group_adeo = models.ForeignKey('ModelGroupAdeo', on_delete=models.PROTECT)

    class Meta:
        ordering = ["code"]
        verbose_name = "модель Адео"
        verbose_name_plural = "Structure_1 модели Адео"

    def __str__(self):
        return self.code


# Attribute
class Attribute(models.Model):
    code = models.CharField(max_length=9, primary_key=True, unique=True)
    is_open = models.BooleanField()
    french_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    russian_name = models.CharField(max_length=200)

    class Meta:
        ordering = ["code"]
        verbose_name = "атрибут"
        verbose_name_plural = "Structure_2 атрибуты"

    def __str__(self):
        return self.code


# Value
class Value(models.Model):
    code = models.CharField(max_length=10, primary_key=True, unique=True)
    french_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    russian_name = models.CharField(max_length=200)

    class Meta:
        ordering = ["code"]
        verbose_name = "значение атрибута"
        verbose_name_plural = "Structure_3 значения атрибутов"

    def __str__(self):
        return self.code


# LMCode
class LMCode(models.Model):
    code = models.CharField(max_length=8, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    avs = models.DateField()
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    class Meta:
        ordering = ["code"]
        verbose_name = "lm код"
        verbose_name_plural = "Structure_4 lm коды"

    def __str__(self):
        return self.code


# Link - принадлежность значений и атрибутов к моделям. Одной записи соответствует одно значение
class Link(models.Model):
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    value = models.ForeignKey(Value, blank=True, on_delete=models.PROTECT)
    link_name = str(model) + " + " + str(attribute) + " + " + str(value)

    class Meta:
        ordering = ["value", "attribute", "model"]
        unique_together = ("model", "attribute", "value")
        verbose_name = "связь"
        verbose_name_plural = "связи"

    def __str__(self):
        return self.link_name
