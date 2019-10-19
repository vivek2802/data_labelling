from django.shortcuts import render,HttpResponse
import pandas as pd
from .models import data_table
# Create your views here.

def data_population(request):
    df = pd.read_csv('train.csv')
    for k in df.Sex:
        data_table.objects.create(items=k,label=None)
    return HttpResponse('data inserted in database')



def data_labelling(request):

    return render(request,'basic.html',{'data':df})