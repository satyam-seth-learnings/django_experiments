from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("print-message/", views.print_message, name="print_message"),
]
