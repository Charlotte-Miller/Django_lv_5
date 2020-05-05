# Template url
from django.conf.urls import url

from web_app import views

app_name = 'web_app'

urlpatterns = [
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
]
