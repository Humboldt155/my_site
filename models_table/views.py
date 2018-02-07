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

from .serializers import \
    DepartmentSerializer, \
    ModelSerializer, \
    AttributeSerializer, \
    ValueSerializer, \
    LMCodeSerializer, \
    LinkSerializer, \
    DepartmentAdeoSerializer, \
    SubDepartmentAdeoSerializer, \
    ModelGroupAdeoSerializer


# Create your views here.


def models_table(request):
    departments = Department.objects.filter()
    return render(request, 'models_list/models_table.html', {'departments': departments})


@csrf_exempt
def department_list(request):
    """
    List all code departments, or create a new department.
    """
    if request.method == 'GET':
        snippets = Department.objects.all()
        serializer = DepartmentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def department_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
