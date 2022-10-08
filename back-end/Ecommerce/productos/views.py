import json
from .models import Bodega, Producto, Tipo
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


class ProductosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            producto = list(Producto.objects.filter(id=id).values())
            if len(producto) > 0:
                lista = producto[0]
                datos = {"message": "Success", "productos": lista}
            else:
                datos = {"message": "No se encontro el Producto ..."}
            return JsonResponse(datos)
        else:
            producto = list(Producto.objects.values())
            if len(producto) > 0:
                datos = {"message": "Success", "productos": producto}
            else:
                datos = {"message": "No se encontraron Productos ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Producto.objects.create(
            nombre=jd["nombre"],
            descripcion=jd["descripcion"],
            stock=jd["stock"],
            tipo_id=jd["tipo"],
            bodega_id=jd["bodega"],
        )
        datos = {"message": "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        producto = list(Producto.objects.filter(id=id).values())
        if len(producto) > 0:
            newProducto = Producto.objects.get(id=id)
            newProducto.nombre = jd["nombre"]
            newProducto.descripcion = jd["descripcion"]
            newProducto.stock = jd["stock"]
            newProducto.tipo_id = jd["tipo"]
            newProducto.bodega_id = jd["bodega"]
            newProducto.save()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Producto no existe..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        producto = list(Producto.objects.filter(id=id).values())
        if len(producto) > 0:
            Producto.objects.filter(id=id).delete()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Producto not found ..."}
        return JsonResponse(datos)


class BodegaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            bodega = list(Bodega.objects.filter(id=id).values())
            if len(bodega) > 0:
                lista = bodega[0]
                datos = {"message": "Success", "bodega": lista}
            else:
                datos = {"message": "No se encontro la bodega ..."}
            return JsonResponse(datos)
        else:
            bodegas = list(Bodega.objects.values())
            if len(bodegas) > 0:
                datos = {"message": "Success", "bodegas": bodegas}
            else:
                datos = {"message": "No se encontraron Bodegas ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Bodega.objects.create(
            nombre=jd["nombre"],
            descripcion=jd["descripcion"],
        )
        datos = {"message": "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        bodega = list(Bodega.objects.filter(id=id).values())
        if len(bodega) > 0:
            newBodega = Bodega.objects.get(id=id)
            newBodega.nombre = jd["nombre"]
            newBodega.descripcion = jd["descripcion"]
            newBodega.save()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Bodega no existe ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        bodega = list(Bodega.objects.filter(id=id).values())
        if len(bodega) > 0:
            Bodega.objects.filter(id=id).delete()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Bodega no existe ..."}
        return JsonResponse(datos)


class TipoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            tipo = list(Tipo.objects.filter(id=id).values())
            if len(tipo) > 0:
                lista = tipo[0]
                datos = {"message": "Success", "tipo": lista}
            else:
                datos = {"message": "No se encontro el tipo ..."}
            return JsonResponse(datos)
        else:
            tipos = list(Tipo.objects.values())
            if len(tipos) > 0:
                datos = {"message": "Success", "tipos": tipos}
            else:
                datos = {"message": "No se encontraron los Tipos ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Tipo.objects.create(
            nombre=jd["nombre"],
            descripcion=jd["descripcion"],
        )
        datos = {"message": "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        tipo = list(Tipo.objects.filter(id=id).values())
        if len(tipo) > 0:
            newTipo = Tipo.objects.get(id=id)
            newTipo.nombre = jd["nombre"]
            newTipo.descripcion = jd["descripcion"]
            newTipo.save()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Tipo no existe ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        tipo = list(Tipo.objects.filter(id=id).values())
        if len(tipo) > 0:
            Tipo.objects.filter(id=id).delete()
            datos = {"message": "Success"}
        else:
            datos = {"message": "Tipo no existe ..."}
        return JsonResponse(datos)
