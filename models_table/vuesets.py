from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

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


from .serializers import \
    DepartmentSerializer, \
    ModelSerializer, \
    AttributeSerializer, \
    ValueSerializer, \
    LMCodeSerializer, \
    LinkSerializer, \
    DepartmentAdeoSerializer, \
    SubDepartmentAdeoSerializer, \
    ModelGroupAdeoSerializer, \
    CodeValueSerializer


class DepartmentVueSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')



class ModelVueSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'french_name', 'english_name', 'russian_name', 'model_group_adeo')


class AttributeVueSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'french_name', 'english_name', 'russian_name')


class ValueVueSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'french_name', 'english_name', 'russian_name')


class LMCodeVueSet(viewsets.ModelViewSet):
    queryset = LMCode.objects.all()
    serializer_class = LMCodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'avs', 'model', 'department')


class LinkVueSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'model', 'attribute', 'value')

class DepartmentAdeoVueSet(viewsets.ModelViewSet):
    queryset = DepartmentAdeo.objects.all()
    serializer_class = DepartmentAdeoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')


class SubDepartmentAdeoVueSet(viewsets.ModelViewSet):
    queryset = SubDepartmentAdeo.objects.all()
    serializer_class = SubDepartmentAdeoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'department_adeo')


class ModelGroupAdeoVueSet(viewsets.ModelViewSet):
    queryset = ModelGroupAdeo.objects.all()
    serializer_class = ModelGroupAdeoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'sub_department_adeo')

class CodeValueVueSet(viewsets.ModelViewSet):
    queryset = CodeValue.objects.all()
    serializer_class = CodeValueSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'lmcode', 'attribute', 'value')