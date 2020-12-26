from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/filial', views.AddFilial),
    path('add/region', views.AddRegion),
    path('add/cekh', views.AddCekh),
    path('add/puo', views.AddPuo),
    path('add/groupitems', views.AddGroupItems),
    path('add/item', views.AddItem),
    path('add/program', views.AddProgram),
    path('add/broadcast', views.AddBroadcast),
    path('add/link', views.AddLink),
    path('filial/<int:id>', views.filial),
]