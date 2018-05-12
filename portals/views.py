from django.shortcuts import render
from django.views.generic import CreateView, ListView
from portals.forms import CreateForm
from django.urls import resolve, reverse_lazy
from portals.models import Discussions

def home(request):
    return render(request, 'portals/HomePage.html')


class CreateItem(CreateView):
    form_class = CreateForm
    template_name = 'portals/navbar.html'
    success_url = reverse_lazy('home_page')



class DisplayItem(ListView):
    model = Discussions
    paginate_by = 20
    template_name = 'portals/lists.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        k = self.kwargs['category']
        items = self.get_queryset().filter(category=k)
        return {'items':items}





