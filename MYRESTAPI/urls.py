from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('',views.myRestView.as_view()),
    path('data/',views.machstatzData.as_view()),
    
]
