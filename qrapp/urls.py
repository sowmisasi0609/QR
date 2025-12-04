from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),
    path('pdf/<int:pk>/', views.pdf_detail, name='pdf_detail'),
]
