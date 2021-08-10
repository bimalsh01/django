from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.from_App),
    path('secondfcn', views.sec_fcn),
    path('index/', views.show_index_page),
    path('second/', views.second_function),
    path('new/', views.new_file)
]