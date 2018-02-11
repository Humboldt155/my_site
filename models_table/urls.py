from django.conf.urls import url, include
from rest_framework import routers
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

from .vuesets import \
    DepartmentVueSet, \
    ModelVueSet, \
    AttributeVueSet, \
    ValueVueSet, \
    LMCodeVueSet, \
    LinkVueSet, \
    DepartmentAdeoVueSet, \
    SubDepartmentAdeoVueSet, \
    ModelGroupAdeoVueSet

router = routers.DefaultRouter()

router.register(r'departments', DepartmentVueSet)
router.register(r'models', ModelVueSet)
router.register(r'attributes', AttributeVueSet)
router.register(r'values', ValueVueSet)
router.register(r'lm_codes', LMCodeVueSet)
router.register(r'links', LinkVueSet)
router.register(r'departments_adeo', DepartmentAdeoVueSet)
router.register(r'sub_departments_adeo', SubDepartmentAdeoVueSet)
router.register(r'model_groups_adeo', ModelGroupAdeoVueSet)


urlpatterns = router.urls
