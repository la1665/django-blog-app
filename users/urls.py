from django.urls import path
from . import views as user_view


urlpatterns = [
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='profile'),

]
