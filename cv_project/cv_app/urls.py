from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from cv_app.sitemaps import Static_Sitemap

sitemaps = {'static' : Static_Sitemap}

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('thanks',views.thanks_view,name='thanks_view'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    ]