from django.utils import timezone
from django.views.generic.list import ListView
from .models import Author


class AuthorList(ListView):
    template_name = 'Authors/author_list'
    queryset = Author.objects.all()

    # another way to do it
    #model = Author

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #return context

