from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_polls2'),
    path('test/', views.test, name='test'),
    path('test_html/', views.test_html, name='test_html'),
    path('casa/test_html_two/', views.test_html_two, name='test_html_two'),
    path('conversor/', views.conversor, name='conversor'),
    path('conversor_cbv/', views.FirstCBView.as_view(), name='conversor_cbv'),
    path('conversor_new/', views.SecondConversor.as_view(), name='conversor_new'),
    path('index_new/', views.IndexView.as_view(), name='index_new'),
    path('index_refactor/', views.TemplateView.as_view(template_name='index.html'), name='index_refactor'),
    path('power_conversor/', views.ConversorSuperPower.as_view(), name='power_conversor'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/new/', views.create_categoria, name='create_categoria')
]