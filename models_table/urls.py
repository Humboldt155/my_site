from django.conf.urls import url
from models_table.views import models_table

urlpatterns = [
    url(r'^$', models_table, name='models_table'),
]