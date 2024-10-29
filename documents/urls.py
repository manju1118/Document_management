from django.urls import path
from . import views





urlpatterns = [
    path('',views.home,name='home'),
    path('upload_document/',views.upload_document,name='upload_document'),
]



