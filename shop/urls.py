from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.index,name="index"),
    path('payout',views.payout,name='payout'),
]
