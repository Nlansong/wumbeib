from django.urls import path
from . import views
from home.views import detail_view


app_name = 'blog'

urlpatterns = [
    path('',views.blog, name='blog'),
    path('<slug:slug>/', detail_view, name='detail'),
]