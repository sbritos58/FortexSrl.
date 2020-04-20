from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Ordenes
from .forms import OrdenesForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from .filters import OrdenesFilter,HistoryFilter
from django.db.models import Sum, Max


class CreateOrdenView(SuccessMessageMixin, CreateView):
    form_class = OrdenesForm
    template_name = 'ordenes/crearOrden.html'

    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_valid(self, form):
        formulario = form.save(commit=False)

        if formulario.estado == 'Entregado' and formulario.ubicacion == 'Cliente':
            formulario.fecha_entrega_real = date.today()
        else:
            formulario.fecha_entrega_real = None
        formulario.usuarios = self.request.user
        messages.success(self.request, '¡¡¡ Orden %s creada correctamente !!!' %(formulario.producto))
        return super().form_valid(form)


def ListViewOrden(request):
    ordenes = Ordenes.objects.filter(estado = 'Entregado')
    historial = Ordenes.history.all()

   #----------------------------------------------- graficas----------------------------------
    totalprod = Ordenes.objects.values_list("producto__nombre").annotate(cantidad=Sum('cantidad_recibida')).order_by('producto')
    totalprodentregados = Ordenes.objects.values_list("producto__nombre").annotate(cantidad=Sum('cantidadEntregada')).order_by('producto')

    totalfechasentregadas = Ordenes.objects.values_list("fecha_entrega_real" ,'producto__nombre', 'cantidadEntregada').order_by('producto')


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
        if totalprod[1] != None:
            productos1.append(i[1])
        else:
            productos1.append(0)
        etiquetas.append(i[0])

    # -------------------------------ESTO ME SERVIA PARA RESTAR DOS LISTAS Y MOSTRARLAS CON NNUMPY ----------------------
    #import numpy as np
    #a = productos1
    #b = listaproductos
    #hola =  list(np.array(b) - np.array(a))
  #-------------------------------------------fin graficas---------------------------------------------



    Model_one = Ordenes.objects.exclude(estado='Entregado',ubicacion='Cliente').order_by('fecha_entrega_estimada')
    total = Model_one.count
    myFilter = OrdenesFilter(request.GET,queryset=Model_one)
    paginator = Paginator(myFilter.qs, 10)
    page = request.GET.get('page1')
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)

    myFilter = OrdenesFilter(request.GET, queryset=Model_one)


    context = {'pub':pub,'myFilter':myFilter,'listatodos':listaTodos,'listaproductos':listaproductos,'listaetiquetas':listaEtiquetas,'productos1':productos1,'etiquetas':etiquetas,'Total':total, 'Model_one': Model_one, 'Ordenes': ordenes,
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


    context = {'Model_one':Model_one,'total':total,'orden':orden,'historial':historial}
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
    form_class = OrdenesForm
    model = Ordenes
    template_name = 'ordenes/updateOrden.html'

    def get_success_url(self):
        return reverse_lazy('listarOrden')

    def form_valid(self, form):


        formulario = form.save(commit=False)
        from Productos.models import Productos
        hola = Productos.objects.get(id=formulario.producto.id)

        print(hola.telaio)
        if(hola.telaio == None):
            Productos.objects.filter(id=formulario.producto.id).update(telaio=formulario.telaio)

            formulario.telaio = formulario.cantidad_recibida / hola.telaio

        else:
            formulario.telaio = formulario.cantidad_recibida / hola.telaio

        if  formulario.estado == 'Completato' and formulario.ubicacion == 'Cliente':
            formulario.fecha_entrega_real = date.today()
            messages.success(self.request, '¡¡¡ La orden %s se ha entregado !!!' % (formulario.orden))


        else:
            formulario.fecha_entrega_real = None
            messages.success(self.request, '¡¡¡ La orden %s se ha modificado correctamente !!!' % (formulario.orden))

        formulario.usuarios = self.request.user



        return super().form_valid(form)


