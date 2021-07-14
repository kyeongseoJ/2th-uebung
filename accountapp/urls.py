from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import wasdenn, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('wasdenn/', wasdenn, name='wasdenn'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create')
]