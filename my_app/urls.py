from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_form_view, name='contact form'),
    path('submission_list/', views.submission_list_view, name='submissions list'),
]