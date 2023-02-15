from django.contrib import admin
from django.urls import path
from asosiy.views import *
# from asosiy.views import result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
