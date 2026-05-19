from django.urls import path
from core.views import login, logout, home, cadastrar_link, listar_links, atualizar_link, remover_link

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('', home, name='home'),

    path('links/cadastrar/', cadastrar_link, name='cadastrar_link'),
    path('links/listar/', listar_links, name='listar_links'),
    path('links/atualizar/<int:pk>/', atualizar_link, name='atualizar_link'),
    path('links/remover/<int:pk>/', remover_link, name='remover_link'),
]