from rest_framework import viewsets

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
    LMCodeAttributeValue

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
    LMCodeAttributeValueSerializer


class DepartmentVueSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ModelVueSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class AttributeVueSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class ValueVueSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class LMCodeVueSet(viewsets.ModelViewSet):
    queryset = LMCode.objects.all()
    serializer_class = LMCodeSerializer


class LinkVueSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class DepartmentAdeoVueSet(viewsets.ModelViewSet):
    queryset = DepartmentAdeo.objects.all()
    serializer_class = DepartmentAdeoSerializer


class SubDepartmentAdeoVueSet(viewsets.ModelViewSet):
    queryset = SubDepartmentAdeo.objects.all()
    serializer_class = SubDepartmentAdeoSerializer


class ModelGroupAdeoVueSet(viewsets.ModelViewSet):
    queryset = ModelGroupAdeo.objects.all()
    serializer_class = ModelGroupAdeoSerializer


class LMCodeAttributeValueVueSet(viewsets.ModelViewSet):
    queryset = LMCodeAttributeValue.objects.all()
    serializer_class = LMCodeAttributeValueSerializer