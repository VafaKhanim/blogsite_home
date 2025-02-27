from django.urls import path
from .views import home_view, about_page
urlpatterns = [
    path('', home_view, name = 'home_view'),
    path('about/', about_page, name = 'about_page')
]