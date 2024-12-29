from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('connect/', views.ConnectPageView.as_view(), name='connect'),
    path('farmerDetail/', views.FarmerDetailPageView, name='farmerDetail'),
    path('farmerRegister/', views.FarmerRegisterPage, name='farmerRegister'),
    path('farmerDetail/farmerReport-pdf/', views.generate_pdf,name='farmerReport-pdf')
]
