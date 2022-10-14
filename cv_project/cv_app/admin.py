from django.contrib import admin
from .models import CV
from .models import Progetto

# from rollyourown.seo.admin import register_seo_admin
# from cv_app.seo import MyMetadata
# register_seo_admin(admin.site, MyMetadata)

# Register your models here.
admin.site.register(CV)
admin.site.register(Progetto)