from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_blog, name='show_blog'),
    path('<int:post_id>/', views.post_details, name='post_details')
]