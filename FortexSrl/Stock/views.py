from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Stock
from .forms import StockForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from django.db.models import Sum, Max
from django.shortcuts import redirect

def ListViewStock(request):
    Model_one = Stock.objects.all()
    context = {'Model_one':Model_one}
    return render(request,'stock/listView.html',context)

def CreateViewStock(request):
    if request.method == 'POST':
        Model_one = StockForm(request.POST)
        if Model_one.is_valid():
            post = Model_one.save(commit=False)
            post.save()
            return redirect('listStock')
    else:
        Model_one = StockForm()
    context = {'Model_one':Model_one}
    return render(request,'stock/crearStock.html',context)