from django.urls import path

from . import views
from .views import inflation_view

app_name = 'app'
urlpatterns = [
    path('', inflation_view, name='main'),
]