
from django.urls import path,include

from todoapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbv/',views.lview.as_view(),name='cbv'),
    path('cbvd/<int:pk>/',views.dview.as_view(),name='cbvd'),
    path('cbvup/<int:pk>/', views.uview.as_view(), name='cbvup'),
    path('cbvdel/<int:pk>/', views.delview.as_view(), name='cbvdel'),

]