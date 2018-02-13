from .models import \
    Department,\
    Model, \
    Attribute,\
    Value, \
    LMCode, \
    Link, \
    DepartmentAdeo, \
    SubDepartmentAdeo, \
    ModelGroupAdeo, \
    CodeValue

import django_filters

class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = ['id', 'name', ]

class ModelFilter(django_filters.FilterSet):
    class Meta:
        model = Model
        fields = ["id", 'french_name', 'english_name', 'russian_name', 'model_group_adeo']

class AttributeFilter(django_filters.FilterSet):
    class Meta:
        model = Attribute
        fields = ['id', 'french_name', 'english_name', 'russian_name']

class ValueFilter(django_filters.FilterSet):
    class Meta:
        model = Value
        fields = ['id', 'french_name', 'english_name', 'russian_name']

class LMCodeFilter(django_filters.FilterSet):
    class Meta:
        model = LMCode
        fields = ['id', 'name', 'avs', 'model', 'department']

class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['id', 'model', 'attribute', 'value']

class DepartmentAdeoFilter(django_filters.FilterSet):
    class Meta:
        model = DepartmentAdeo
        fields = ['id', 'name']

class SubDepartmentAdeoFilter(django_filters.FilterSet):
    class Meta:
        model = SubDepartmentAdeo
        fields = ['id', 'name', 'department_adeo']


class ModelGroupAdeoFilter(django_filters.FilterSet):
    class Meta:
        model = ModelGroupAdeo
        fields = ['id', 'name', 'sub_department_adeo']


class CodeValueFilter(django_filters.FilterSet):
    class Meta:
        model = CodeValue
        fields = ['id', 'lmcode', 'attribute', 'value']