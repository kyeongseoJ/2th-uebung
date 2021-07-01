from django.urls import path

from accountapp.views import wasdenn

app_name = 'accountapp'

urlpatterns = [
    path('wasdenn/', wasdenn, name='wasdenn')
]