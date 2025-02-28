from django.urls import path
from .views import home_view, about_page, post_detail
urlpatterns = [
    path('', home_view, name = 'home_view'),
    path('about/', about_page, name = 'about_page'),
    path('post/<int:post_id>/', post_detail, name='post_detail')
]