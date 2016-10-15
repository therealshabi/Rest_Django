from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from tester.models import Details
from tester.serializers import DetailSerializer


def index(request):
    context_dict = {}
    try:
        name_list = Details.objects.all()
        context_dict['Name'] = name_list

    except Details.DoesNotExist:
        context_dict['Name'] = None
    return render(request, 'tester/index.html', context=context_dict)
    #   return HttpResponse("Done Successfully")


def check(request):
    if request.method == 'POST':
        form = Details(request.POST)
        form.save(commit=True)
    return index(request)


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer
