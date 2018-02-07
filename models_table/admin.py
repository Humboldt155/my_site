from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Department
from .models import Model
from .models import Attribute
from .models import Value
from .models import LMCode
from .models import Link
from .models import DepartmentAdeo
from .models import SubDepartmentAdeo
from .models import ModelGroupAdeo
from .models import LMCodeAttributeValue

from .resources import DepartmentResource
from .resources import ModelResource
from .resources import AttributeResource
from .resources import ValueResource
from .resources import LMCodeResource
from .resources import LinkResource
from .resources import DepartmentAdeoResource
from .resources import SubDepartmentAdeoResource
from .resources import ModelGroupAdeoResource
from .resources import LMCodeAttributeValueResource


#admin.site.register(Department)
#admin.site.register(DepartmentAdeo)
#admin.site.register(SubDepartmentAdeo)
#admin.site.register(ModelGroupAdeo)
#admin.site.register(Model)
#admin.site.register(Attribute)
#admin.site.register(Value)
#admin.site.register(LMCode)
#admin.site.register(Link)
#admin.site.register(LMCodeAttributeValue)

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    pass


@admin.register(DepartmentAdeo)
class DepartmentAdeoAdmin(ImportExportModelAdmin):
    pass


@admin.register(SubDepartmentAdeo)
class SubDepartmentAdeoAdmin(ImportExportModelAdmin):
    pass


@admin.register(ModelGroupAdeo)
class ModelGroupAdeoAdmin(ImportExportModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(ImportExportModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Value)
class ValueAdmin(ImportExportModelAdmin):
    pass


@admin.register(LMCode)
class LMCodeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(ImportExportModelAdmin):
    pass


@admin.register(LMCodeAttributeValue)
class LMCodeAttributeValueAdmin(ImportExportModelAdmin):
    pass

