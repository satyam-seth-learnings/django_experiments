from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("send-test-email/", views.send_test_email, name="send_test_email"),
    path(
        "send-prod-smtp-email/",
        views.send_prod_smtp_email,
        name="send_prod_smtp_email",
    ),
    path("send-prod-api-email/", views.send_prod_api_email, name="send_prod_api_email"),
]
