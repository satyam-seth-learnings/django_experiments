from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "myapp/home.html")


# Send Test Email (Dev)
def send_test_email(self):
    subject = "Test Email"
    name = "User"
    html_message = render_to_string("myapp/email_template.html", {"name": name})
    plain_message = strip_tags(html_message)
    from_email = "admin@example.com"
    to_email = ["user@example.com"]

    # Create email with Plain Text Message
    email = EmailMessage(
        subject=subject, body=plain_message, from_email=from_email, to=to_email
    )

    # Send the email
    email.send()

    return HttpResponse("Test email with Plain Message sent successfully.")
