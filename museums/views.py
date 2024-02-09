from django.shortcuts import render
from museums.models import Museum

def museum_index(request):
    museums = Museum.objects.all()
    context = {
        "museums": museums
    }
    return render(request, 'museums/museum_index.html', context)

def museum_detail(request, pk):
    museum = Museum.objects.get(pk=pk)
    context = {
        "museum": museum
    }
    return render(request, 'museums/museum_detail.html', context)

