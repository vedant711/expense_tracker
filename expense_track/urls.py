from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('logout', views.logout, name='logout'),

    path('<id>', views.dashboard, name='dashboard'),
    path('credit/<id>', views.credit, name='credit'),
    path('debit/<id>', views.debit, name='debit'),
    path('transfer/<id>', views.transfer, name='transfer'),




]