#-*- coding:utf-8 -*-

from django.shortcuts import render

from .models import item
from .forms import searchForm
from .forms import updateForm
from .forms import uploadFileForm
from .parse import parse

def item_main(request):
    results = "품종: %d" % (item.objects.count())
    form = searchForm()

    return render(request, 'check/main.html', {'form': form, 'results': results})

def item_update(request):
    results = []
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('temp.txt', 'wb') as destination:
                for chunk in request.FILES['file']:
                    destination.write(chunk)
                results = parse('temp.txt')
    else:
        form = uploadFileForm()

    return render(request, 'check/update.html', {'form': form, 'results': results})

def item_search(request):
    results = []
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            query_type = form.cleaned_data['query_type']
            query_text = form.cleaned_data['query_text']

            if query_type == 'no':
                querySet = item.objects.filter(no__icontains=query_text)
            elif query_type == 'name':
                querySet = item.objects.filter(name__icontains=query_text)
            elif query_type == 'description':
                querySet = item.objects.filter(description__icontains=query_text)
                
            for result in querySet:
                results.append(result)
            if len(results) == 0:
                results.append('no result')
    else:
        form = searchForm()
    return render(request,'check/search.html', {'form': form, 'results': results})
