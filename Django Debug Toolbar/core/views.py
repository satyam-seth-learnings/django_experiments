from django.views.generic import ListView
from .models import Student

# Create your views here.


class StudentListView(ListView):
    """Student List View"""

    model = Student
