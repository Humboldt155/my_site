from import_export import resources
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


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


class ModelResource(resources.ModelResource):
    class Meta:
        model = Model


class AttributeResource(resources.ModelResource):
    class Meta:
        model = Attribute


class ValueResource(resources.ModelResource):
    class Meta:
        model = Value


class LMCodeResource(resources.ModelResource):
    class Meta:
        model = LMCode


class LinkResource(resources.ModelResource):
    class Meta:
        model = Link


class DepartmentAdeoResource(resources.ModelResource):
    class Meta:
        model = DepartmentAdeo


class SubDepartmentAdeoResource(resources.ModelResource):
    class Meta:
        model = SubDepartmentAdeo


class ModelGroupAdeoResource(resources.ModelResource):
    class Meta:
        model = ModelGroupAdeo


class LMCodeAttributeValueResource(resources.ModelResource):
    class Meta:
        model = LMCodeAttributeValue
