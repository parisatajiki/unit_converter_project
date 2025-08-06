from django.urls import path
from .views import Home, Weight_converter ,Length_converter,Temperature_converter

app_name = "converter_app"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('weight', Weight_converter.as_view(), name='weight'),
    path('temperature', Temperature_converter.as_view(), name='temperature'),
    path('length',Length_converter.as_view(), name='length'),
]