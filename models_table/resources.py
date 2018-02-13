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
    CodeValue

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        skip_unchanged = True
        report_skipped = False


class ModelResource(resources.ModelResource):
    class Meta:
        model = Model
        skip_unchanged = True
        report_skipped = False


class AttributeResource(resources.ModelResource):
    class Meta:
        model = Attribute
        skip_unchanged = True
        report_skipped = False


class ValueResource(resources.ModelResource):
    class Meta:
        model = Value
        skip_unchanged = True
        report_skipped = False


class LMCodeResource(resources.ModelResource):
    class Meta:
        model = LMCode
        skip_unchanged = True
        report_skipped = False


class LinkResource(resources.ModelResource):
    class Meta:
        model = Link
        skip_unchanged = True
        report_skipped = False


class DepartmentAdeoResource(resources.ModelResource):
    class Meta:
        model = DepartmentAdeo
        skip_unchanged = True
        report_skipped = False


class SubDepartmentAdeoResource(resources.ModelResource):
    class Meta:
        model = SubDepartmentAdeo
        skip_unchanged = True
        report_skipped = False


class ModelGroupAdeoResource(resources.ModelResource):
    class Meta:
        model = ModelGroupAdeo
        skip_unchanged = True
        report_skipped = False

class CodeValueResource(resources.ModelResource):
    class Meta:
        model = CodeValue
        skip_unchanged = True
        report_skipped = False