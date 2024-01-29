from django.urls import path
from . import views


urlpatterns = [
    path('novo_produto/',  views.novo_produto, name='novo_produto'),
    path('listar_produtos/',  views.listar_produtos, name='listar_produtos'),
    path('editar_produto/<int:id>/',  views.editar_produto, name='editar_produto'),
]