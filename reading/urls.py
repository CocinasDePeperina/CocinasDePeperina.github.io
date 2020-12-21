from django.conf.urls import url
from django.views.generic import RedirectView
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='pagina_principal/', permanent=True)),
    path('pagina_principal/', views.index, name='Peperina-home'),
    re_path(r'(?P<r_Name>[\w.@+-]+)/(?P<r_Id>\d+)', views.about, name='receta'),
]
