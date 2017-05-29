#-*- coding:utf-8 -*-

import os

from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from .models import item
from .forms import searchForm
from .forms import updateForm
from .forms import uploadFileForm
from .parse import parse

#TEMP_FILE = os.path.join(os.getcwd(), 'temp.txt')
TEMP_FILE = '/home/younguk/work/warehouse/temp.txt'

def item_main(request):
    results = []
    results_num = item.objects.count()
    for result in item.objects.order_by('-updateDate')[:20]:
        if result.amount != 0:
            results.append(result)

    return render(request, 'check/main.html', {'results_num': results_num, 'results': results})

def item_update(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open(TEMP_FILE, 'wb') as destination:
                for chunk in request.FILES['file']:
                    destination.write(chunk)
                errors, results = parse(TEMP_FILE)
                return render(request, 'check/update.html', {'form': form, 'errors': errors, 'results': results})
    else:
        form = uploadFileForm()
        return render(request, 'check/update.html', {'form': form})

def item_search(request):
    results = []
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            query_plant = form.cleaned_data['query_plant']
            query_type = form.cleaned_data['query_type']
            query_text = form.cleaned_data['query_text']
            query_num = '-1'
            
            if query_type == 'no':
                querySet = item.objects.filter(no__icontains=query_text, Plnt=query_plant)
            elif query_type == 'name':
                querySet = item.objects.filter(name__icontains=query_text, Plnt=query_plant)
            elif query_type == 'description':
                querySet = item.objects.filter(description__icontains=query_text, Plnt=query_plant)

            results_num = querySet.count()    
            for result in querySet:
                results.append(result)

    elif request.method == 'GET':
        form = searchForm()
        try:
            query_plant = request.GET['query_plant']
            query_type = request.GET['query_type']
            query_text = request.GET['query_text']
            query_num = request.GET['query_num']

            if query_type == 'no':
                querySet = item.objects.filter(no__icontains=query_text, Plnt=query_plant)
            elif query_type == 'name':
                querySet = item.objects.filter(name__icontains=query_text, Plnt=query_plant)
            elif query_type == 'description':
                querySet = item.objects.filter(description__icontains=query_text, Plnt=query_plant)

            results_num = querySet.count()   
            for result in querySet:
                results.append(result)

            if query_num != '0':
                results = results[10*(int(query_num)-1):10*int(query_num)]

        except KeyError:
            results_num = 0
            query_num = '-1'

    if results_num == 0:
        results.append('no result')

    if request.method == 'GET':
        if query_num == '0' and results_num != 0:
            return JsonResponse({ 'no': results[0].no,
                              'name': results[0].name,
                              'description': results[0].description,
                              'amount': results[0].amount,
                              'slot': results[0].slot,
                               })
        else:
            return render(request,'check/search.html', {'form': form, 'results_num': results_num, 'results': results}) 
    else:
        return render(request,'check/search.html', {'form': form, 'results_num': results_num, 'results': results})
