from django.contrib import admin

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

admin.site.register(Department)

admin.site.register(DepartmentAdeo)
admin.site.register(SubDepartmentAdeo)
admin.site.register(ModelGroupAdeo)
admin.site.register(Model)
admin.site.register(Attribute)
admin.site.register(Value)
admin.site.register(LMCode)
admin.site.register(Link)
admin.site.register(LMCodeAttributeValue)
