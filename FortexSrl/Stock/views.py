from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from Ordenes.models import Ordenes
from .models import Stock, StockMovimientos
from .forms import StockForm, StockMovimientosForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from django.db.models import Sum, Max
from django.http import JsonResponse
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from .filters import OrdenesFilter, StockMovimientosFilter


def ListViewStock(request):
    Model_one = Stock.objects.all().order_by("cantidad")

    myFilter = OrdenesFilter(request.GET, queryset=Model_one)
    paginator = Paginator(myFilter.qs, 10)
    page = request.GET.get('page1')
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)

    myFilter = OrdenesFilter(request.GET, queryset=Model_one)

    context = {'Model_one': Model_one, 'pub': pub, "myFilter": myFilter}
    return render(request, 'stock/listView.html', context)


def ListViewMovimientosStock(request):
    Model_one = StockMovimientos.objects.all()

    myFilter = StockMovimientosFilter(request.GET, queryset=Model_one)
    paginator = Paginator(myFilter.qs, 10)
    page = request.GET.get('page1')
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)

    myFilter = StockMovimientosFilter(request.GET, queryset=Model_one)

    context = {'Model_one': Model_one, 'pub': pub, "myFilter": myFilter}
    return render(request, 'stock/ListaCambios.html', context)


def CreateViewStock(request):
    if request.method == 'POST':
        Model_one = StockForm(request.POST)
        if Model_one.is_valid():
            post = Model_one.save(commit=False)
            post.save()
            return redirect('listStock')
    else:
        Model_one = StockForm()
    context = {'Model_one': Model_one}
    return render(request, 'stock/crearStock.html', context)


def CreateView(request, pk):
    ordenFormSet = inlineformset_factory(Ordenes, StockMovimientos, fields='__all__', extra=8)

    orden = Ordenes.objects.get(orden=pk)
    formset = ordenFormSet()

    hola = Stock.objects.all()

    if request.method == "POST":

        formset = ordenFormSet(request.POST, instance=orden)

        f = formset.cleaned_data
        producto = []
        for i in formset:
            producto.append(i)
        cosas = []
        for j in producto:

            if j.cleaned_data.get("nombre") not in cosas and j.cleaned_data.get("nombre") != None:
                cantidad = j.cleaned_data.get("cantidad")
                producto1 = j.cleaned_data.get("nombre")
                producto = Stock.objects.get(id=producto1.id)
                productoStock = producto.cantidad
                if productoStock - cantidad > -1:

                    if formset.is_valid():
                        for f in formset:
                            cd = f.cleaned_data

                            cantidad = cd.get("cantidad")
                            if cantidad != None:
                                producto = cd.get("nombre")
                                orden = cd.get("orden")

                                producto = Stock.objects.get(id=producto.id)
                                productoStock = producto.cantidad
                                movimiento = cd.get("tipo_de_movimiento")
                                if movimiento == True:
                                    suma = productoStock + cantidad
                                    Stock.objects.filter(id=producto.id).update(cantidad=suma)
                                    messages.success(request, "È stato registrato la somma del prodotto" + producto.nombre + ", quantità: " + str(cantidad) + " G.")

                                else:
                                    resta = productoStock - cantidad
                                    Stock.objects.filter(id=producto.id).update(cantidad=resta)
                                    messages.success(request, "È stato registrata la resta del prodotto " + producto.nombre + ", quantità: " + str(cantidad) + " G.")

                        formset.save()

                        return redirect('listStock')

                else:
                    messages.success(request, "Il stock del prodotto " + producto1.nombre + " non puo essere meno di 0, Ora " + str(productoStock)+" G.")
    context = {"form": formset, "orden": orden}
    return render(request, 'stock/crearStock2.html', context)


class UpdateStock(UpdateView):
    form_class = StockForm
    model = Stock
    template_name = "stock/updateStock.html"

    def get_success_url(self):
        return reverse_lazy('listStock')
