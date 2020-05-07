from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Ordenes
from .forms import OrdenesForm, UpdateOrdenesForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from .filters import OrdenesFilter, HistoryFilter
from django.db.models import Sum, Max
from operator import sub
from Stock.models import StockMovimientos,Stock

def ListarEntregadosView(request):
    Model_one = Ordenes.objects.all().filter(estado='Completato')

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
    return render(request, 'ordenes/listarEntregados.html', context)


def dashboard(request):

    # todo crear entregados por mes

    # variables globales para pasar a dashboard
    totalUsado = StockMovimientos.objects.filter(tipo_de_movimiento=False).annotate(Sum("cantidad"))
    totalprod = Ordenes.objects.values_list("producto__nombre").exclude(cantidadEntregada=None).annotate(cantidad=Sum('cantidad_recibida')).order_by('producto')
    totalprodentregados = Ordenes.objects.values_list("producto__nombre").exclude(cantidadEntregada=None).annotate(cantidad=Sum('cantidadEntregada')).order_by('producto')
    totalprodentregados2 = Ordenes.objects.all().exclude(cantidadEntregada=None).annotate(cantidad=Sum("cantidadEntregada"))

    #funciones para recuperar datos a mostrar

    totalUsadoCant = []
    totalUsadoEtiq = []
    for i in totalUsado:
        totalUsadoEtiq.append(i.nombre)
        totalUsadoCant.append(i.cantidad)

    productos1 = []
    for i in totalprod:
        if totalprod[0] != None:
            productos1.append(i[1])
        else:
            productos1.append(0)

    productos2 = []
    listatitulos = []
    for i in totalprodentregados:
        if i[1] != None:
            listatitulos.append(i[0])

            productos2.append(i[1])
        else:
            listatitulos.append(i[0])
            productos2.append(0)

    total = list(map(int.__sub__,productos2,productos1))

    context = {"total": total,"etiquetas":listatitulos,"totalProdEntr":totalprodentregados2,"totalUsadoEtiq":totalUsadoEtiq,'totalUsadoCant':totalUsadoCant}
    return render(request, 'ordenes/dashboard.html', context)




class CreateOrdenView(SuccessMessageMixin, CreateView):
    form_class = OrdenesForm
    template_name = 'ordenes/crearOrden.html'

    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_valid(self, form):
        formulario = form.save(commit=False)

        if formulario.estado == 'Entregado':
            formulario.fecha_entrega_real = date.today()
        else:
            formulario.fecha_entrega_real = None
        formulario.usuarios = self.request.user
        messages.success(self.request, '¡¡¡ Orden %s creada correctamente !!!' % (formulario.producto))
        return super().form_valid(form)


def ListViewOrden(request):
    ordenes = Ordenes.objects.filter(estado='Entregado')
    historial = Ordenes.history.all()
    # ----------------------------------------------- graficas----------------------------------
    totalprod = Ordenes.objects.values_list("producto__nombre").annotate(cantidad=Sum('cantidad_recibida')).order_by('producto')
    totalprodentregados = Ordenes.objects.values_list("producto__nombre").annotate(cantidad=Sum('cantidadEntregada')).order_by('producto')
    totalfechasentregadas = Ordenes.objects.values_list("fecha_entrega_real", 'producto__nombre', 'cantidadEntregada').order_by('producto')
    listaTodos = []
    listaproductos = []
    listaEtiquetas = []

    for i in totalfechasentregadas:
        if i[0] != None:
            listaTodos.append(i)

    print(listaTodos)

    for i in totalprodentregados:
        if i[1] != None:
            listaproductos.append(i[1])
        else:
            listaproductos.append(0)

        listaEtiquetas.append(i[0])
    productos1 = []
    etiquetas = []

    for i in totalprod:
        if totalprod[0] != None:
            productos1.append(i[1])
        else:
            productos1.append(0)
        etiquetas.append(i[0])
    fuera = ("Completato", "Entregado")

    Model_one = Ordenes.objects.exclude(estado__in=fuera).order_by('fecha_entrega_estimada')
    total = Model_one.count
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
    comparar = date.today()
    fechasAcomparar = []
    for i in Model_one:
        fechasAcomparar.append(str(abs(comparar - i.fecha_entrega_estimada).days) + " dias" + " " + str(i.orden))

    print(fechasAcomparar)
    context = {'pub': pub, 'myFilter': myFilter, 'listatodos': listaTodos, 'listaproductos': listaproductos, 'listaetiquetas': listaEtiquetas, 'productos1': productos1, 'etiquetas': etiquetas, 'Total': total, 'Model_one': Model_one, 'Ordenes': ordenes,
               'History': historial}
    return render(request, 'ordenes/ListarOrden.html', context)


def ListHistorialView(request):
    porOrden = Ordenes.history.values_list("orden").annotate(cantidad=Sum('history_id'))

    orden = []
    historial = []
    for i in porOrden:
        historial.append(i[1])
        orden.append(i[0])

    Model_one = Ordenes.history.all().order_by('history_id')
    total = Model_one.count
    paginator = Paginator(Model_one, 10)
    page = request.GET.get('page1')
    try:
        Model_one = paginator.page(page)
    except PageNotAnInteger:
        Model_one = paginator.page(1)
    except EmptyPage:
        Model_one = paginator.page(paginator.num_pages)

    context = {'Model_one': Model_one, 'total': total, 'orden': orden, 'historial': historial}
    return render(request, 'ordenes/history.html', context)


class DetailOrdenView(DetailView):
    form_class = OrdenesForm
    model = Ordenes
    template_name = 'ordenes/detailOrden.html'


class DeleteOrdenView(DeleteView):
    model = Ordenes

    def get_success_url(self):
        success_message = '¡¡¡ Producto eliminado correctamente !!!'
        messages.success(self.request, (success_message))
        return reverse_lazy('listarOrden')


class UpdateOrdenView(UpdateView):
    form_class = UpdateOrdenesForm
    model = Ordenes
    template_name = 'ordenes/updateOrden.html'



    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_invalid(self, form):
        print("errrrrorororororo")
        print(form)
        return super().form_invalid(form)

    def form_valid(self, form):
        formulario = form.save(commit=False)
        from Productos.models import Productos

        print(formulario)  # 3
        print(form)

        hola = Productos.objects.get(id=formulario.producto.id)

        print(hola)

        if (hola.telaio == None):
            print("Aca estoy pero no tengo que hacer nada")
            Productos.objects.filter(id=formulario.producto.id).update(telaio=formulario.telaio)
            formulario.telaio = formulario.cantidad_recibida / formulario.telaio

        else:
            pass

        if formulario.estado == 'Completato':
            formulario.fecha_entrega_real = date.today()
            messages.success(self.request, "¡¡¡ L'ordine %s è stato consegnato !!!" % (formulario.orden))


        else:
            formulario.fecha_entrega_real = None
            messages.success(self.request, "¡¡¡ L'ordine %s è stato aggiornato correttamente !!!" % (formulario.orden))

        formulario.usuarios = self.request.user

        return super().form_valid(form)
