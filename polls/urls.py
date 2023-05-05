from django.urls import path, register_converter
from . import converters, views
register_converter(converters.FourDigitYearConverter, 'yyyy')
app_name = 'polls'
urlpatterns = [
    path('demo/<yyyy:year>/', views.demo, name='demo')
]