from django.shortcuts import render
from .models import Department

# Create your views here.


def models_table(request):
    departments = Department.objects.filter()
    return render(request, 'models_list/models_table.html', {'departments': departments})
