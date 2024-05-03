from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_cat, name='all_cat'),
    path('<slug:c_slug>/', views.all_cat, name='prod_by_cat'),
    path('<slug:c_slug>/<slug:p_slug>/', views.pro_details, name="prod_details")

]
