from django.urls import path

from itis_app.views import index

app_name = 'itis_app'

urlpatterns = [
    path('', index, name='index'),
]
