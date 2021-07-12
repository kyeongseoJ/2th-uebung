from django.urls import path

from accountapp.views import wasdenn, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('wasdenn/', wasdenn, name='wasdenn'),

    path('create/', AccountCreateView.as_view(), name='create')
]