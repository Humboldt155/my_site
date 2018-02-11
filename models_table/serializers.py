"""Первое, что нам нужно сделать с веб-API,
- предоставить способ сериализации и десериализации
экземпляров фрагмента в представлениях, таких как json.
Мы можем сделать это, объявив сериализаторы,
которые очень похожи на формы Django."""

from rest_framework import serializers
from .models import \
    Department,\
    Model, \
    Attribute,\
    Value, \
    LMCode, \
    Link, \
    DepartmentAdeo, \
    SubDepartmentAdeo, \
    ModelGroupAdeo


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", 'name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ["id", 'french_name', 'english_name', 'russian_name', 'model_group_adeo']

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["id", 'french_name', 'english_name', 'russian_name']


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", 'french_name', 'english_name', 'russian_name']

class LMCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMCode
        fields= ['id', 'name', 'avs', 'model', 'department']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'model', 'attribute', 'value']

class DepartmentAdeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentAdeo
        fields = ["id", 'name']


class SubDepartmentAdeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartmentAdeo
        fields = ["id", 'name', 'department_adeo']


class ModelGroupAdeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelGroupAdeo
        fields = ["id", 'name', 'sub_department_adeo']
