from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/',views.base, name='base'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.index, name='index'),
    path('aluno/<int:id>',views.aluno, name='aluno'),
    path('entrada/', views.entrada, name='entrada')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)