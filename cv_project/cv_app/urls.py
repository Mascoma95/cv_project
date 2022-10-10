from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('thanks',views.thanks_view,name='thanks_view'),
    ]