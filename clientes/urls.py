from django.urls import path
from .views import cadastrar_cliente, listar_clientes, detalhes_cliente, atualizar_cliente, excluir_cliente

urlpatterns = [
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/', listar_clientes, name='listar_clientes'),
    path('<int:pk>/', detalhes_cliente, name='detalhes_cliente'),
    path('<int:pk>/atualizar/', atualizar_cliente, name='atualizar_cliente'),
    path('<int:pk>/excluir/', excluir_cliente, name='excluir_cliente'),
]
