from django.shortcuts import render
from django.core.mail import EmailMessage, EmailMultiAlternatives
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

    # # Create email with Plain Text Message
    # email = EmailMessage(
    #     subject=subject,
    #     body=plain_message,
    #     from_email=from_email,
    #     to=to_email,
    # )

    # # Create email with HTML Content
    # email = EmailMessage(
    #     subject=subject,
    #     body=html_message,
    #     from_email=from_email,
    #     to=to_email,
    # )
    # email.content_subtype = "html"  # Set the email content type to HTML

    # Create the email message with both plain text and HTML content
    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_email,
        to=to_email,
    )
    email.attach_alternative(html_message, "text/html")

    # Send the email
    email.send()

    return HttpResponse(
        "Test email with Plain Message,  HTML Content and Attachment sent successfully."
    )
