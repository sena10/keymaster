from django.urls import path
from key_aplication import views


urlpatterns = [
    path('chaves/', views.list_chaves,name='list_chaves'),
    path('list_indisponiveis/', views.list_indisponiveis,name='list_indisponiveis'),
    path('list_disponiveis/', views.list_disponiveis,name='list_disponiveis'),
    path('alugado/', views.alugado,name='alugado'),
    path('devolver/', views.devolver,name='devolver'),
    path('chaves/pegar/<int:chave_id>/', views.alugar_chave, name='alugar_chave'),
    path('chaves/devolver/<int:chave_id>/',views.devolver_chave, name='devolver_chave'),
    #path('login/', views.loginpage,name='login'),
    #path('logout/', views.logoutpage,name='logout'),
    # path('principal2/', views.principalpage,name='principal2'),
    path("accounts/registration/", views.Registration.as_view(), name="registration"),
    path('agradecimento/', views.agradecimento, name='agradecimento'),
    #path("accounts/login/", views.loginpage, name="login")
    #path('chaves/', views.lista_chaves, name='listar_chaves'),

]
