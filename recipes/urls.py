from .views import IndexView, create_view, RegistrationView, ProtectedAboutView
from django.urls import path

app_name = 'recipes'
urlpatterns = [
    path('', IndexView, name='home'),
    path('about/', ProtectedAboutView.as_view(), name='about'),
    path('create/', create_view, name='create_view'),
    path('register/', RegistrationView.as_view(), name='register'),

]