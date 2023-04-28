from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alugueis, name='listar_alugueis'),
    path('novo/', views.novo_aluguel, name='novo_aluguel'),
    path('agendadetalhes_aluguel/<int:pk>/', views.detalhes_aluguel, name='detalhes_aluguel'), 
    path('<int:pk>/excluir/', views.excluir_aluguel, name='excluir_aluguel'),
]
