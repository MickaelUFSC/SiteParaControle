from django.urls import path
from . import views


urlpatterns = [
    path('nova_venda/',  views.nova_venda, name='nova_venda'),
]