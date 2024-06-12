from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .models import Post
from .forms import FormatForm
from .admin import PostResource

# Create your views here.

class PostListView(ListView, FormView):
    model = Post
    template_name = 'posts/main.html'
    form_class = FormatForm

    def post(self, request, **kwargs):
        qs = self.get_queryset()
        dataset = PostResource().export(qs)
        
        format = request.POST.get('format')
        
        if format == 'xls':
            ds = dataset.xls
        elif format == 'csv':
            ds = dataset.csv
        else:
            ds = dataset.json

        response = HttpResponse(ds, content_type=format)
        response['Content-Disposition'] = f"attachment; filename=post.{format}"
        return response