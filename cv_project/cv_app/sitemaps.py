from django.contrib.sitemaps import Sitemap

from cv_app.models import Progetto,CV

from django.urls import reverse

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['home_view','thanks_view']

    def location(self, item):
        return reverse(item)
