from django.contrib import admin
from django.urls import path
from django.conf import settings    #media locals
from django.conf.urls.static import static #static app

import art.views
import blog.views

urlpatterns = [
    path('aboutMe', blog.views.aboutMe, name='aboutMe'),
    path('store', art.views.store, name='store'),
    path('portfolio', art.views.portfolio, name='portfolio'),
    path('blogs/',blog.views.blogs, name='blogs'),
    path('blogs/detail',blog.views.detail,name='detail'),
    path('admin/', admin.site.urls),
    path('',art.views.home, name='home'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #implements media locals
