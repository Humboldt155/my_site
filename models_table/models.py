from django.db import models


class Department(models.Model):
    id = models.CharField(max_length=2, primary_key=True, unique=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["id"]
        verbose_name = "LMRussia отдел"
        verbose_name_plural = "LMRussia_1 отделы"

    def __str__(self):
        return str(self.id)


class DepartmentAdeo(models.Model):
    id = models.CharField(max_length=6, primary_key=True, unique=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["id"]
        verbose_name = "отдел Adeo"
        verbose_name_plural = "Adeo_1 отделы"

    def __str__(self):
        return self.id


class SubDepartmentAdeo(models.Model):
    id = models.CharField(max_length=12, primary_key=True, unique=True)
    name = models.CharField(max_length=60)
    department_adeo = models.ForeignKey(DepartmentAdeo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "подотдел Adeo"
        verbose_name_plural = "Adeo_2 подотделы"

    def __str__(self):
        return self.id


class ModelGroupAdeo(models.Model):
    id = models.CharField(max_length=14, primary_key=True, unique=True)
    name = models.CharField(max_length=60, verbose_name="Название")
    sub_department_adeo = models.ForeignKey(SubDepartmentAdeo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "Adeo группа моделей"
        verbose_name_plural = "Adeo_3 группы моделей"

    def __str__(self):
        return str(self.id)


# Model Adeo
class Model(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    french_name = models.CharField(max_length=200, blank=True, null=True)
    english_name = models.CharField(max_length=200, blank=True, null=True)
    russian_name = models.CharField(max_length=200, blank=True, null=True)
    model_group_adeo = models.ForeignKey(ModelGroupAdeo, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "модель Адео"
        verbose_name_plural = "Structure_1 модели Адео"

    def __str__(self):
        return str(self.id)


# Attribute
class Attribute(models.Model):
    id = models.CharField(max_length=9, primary_key=True, unique=True)
    is_open = models.BooleanField()
    french_name = models.CharField(max_length=200, blank=True, null=True)
    english_name = models.CharField(max_length=200, blank=True, null=True)
    russian_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "атрибут"
        verbose_name_plural = "Structure_2 атрибуты"

    def __str__(self):
        return self.id


# Value
class Value(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    french_name = models.CharField(max_length=200, blank=True, null=True)
    english_name = models.CharField(max_length=200, blank=True, null=True)
    russian_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "значение атрибута"
        verbose_name_plural = "Structure_3 значения атрибутов"

    def __str__(self):
        return str(self.id)


# LMCode
class LMCode(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    avs = models.DateField(blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "lm код"
        verbose_name_plural = "Structure_4 lm коды"

    def __str__(self):
        return str(self.id)


# Link - принадлежность значений и атрибутов к моделям. Одной записи соответствует одно значение
class Link(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["value", "attribute", "model"]
        verbose_name = "связь"
        verbose_name_plural = "связи"

class CodeValue(models.Model):
    lmcode = models.ForeignKey(LMCode, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["lmcode"]
        verbose_name = "Значение для кода"
        verbose_name_plural = "Значения для кодов"
