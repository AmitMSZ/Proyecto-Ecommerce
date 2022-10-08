from django.urls import path
from .views import BodegaView, ProductosView, TipoView

urlpatterns = [
    path("", ProductosView.as_view(), name="productos"),
    path("<int:id>", ProductosView.as_view(), name="producto"),
    path("bodega/", BodegaView.as_view(), name="bodegas"),
    path("bodega/<int:id>", BodegaView.as_view(), name="bodega"),
    path("tipo/", TipoView.as_view(), name="tipos"),
    path("tipo/<int:id>", TipoView.as_view(), name="tipo"),
]
