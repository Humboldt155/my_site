from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import \
    Department, \
    Model, \
    Attribute, \
    Value, \
    LMCode, \
    Link, \
    DepartmentAdeo, \
    SubDepartmentAdeo, \
    ModelGroupAdeo

# Create your views here.
