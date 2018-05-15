from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, DetailView, FormView, View
from portals.forms import CreateForm, ReplyForm, UserForm
from django.urls import resolve, reverse_lazy
from portals.models import Discussions, Replies
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from pusher import Pusher
from django.views.decorators.csrf import csrf_exempt

app_id = "526161"
key = "d265b7301a055c552106"
secret = "8759168a5e5e47dfa43a"
cluster = "ap2"

pusher = Pusher(app_id=app_id, key=key, secret=secret)


def home(request):
    return render(request, 'portals/HomePage.html')


class CreateItem(CreateView):
    form_class = CreateForm
    template_name = 'portals/navbar.html'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']


class DisplayItem(ListView):
    model = Discussions
    paginate_by = 10
    template_name = 'portals/lists.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return super().get_queryset().filter(category=self.kwargs.get('category'), description__icontains=query)


class DiscussItem(ListView):
    model = Replies
    template_name = 'portals/discuss.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(replied_to=self.kwargs.get('key'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['root'] = Discussions.objects.get(pk = self.kwargs.get('key'))
        context['form'] = ReplyForm(self.request.GET)
        return context


class AddReply(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    template_name = 'portals/discuss.html'
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        reply_instance = form.save()
        reply_instance.replied_to.add(self.kwargs['key'])
        return super().form_valid(form)


class LoginUser(FormView):
    form_class = UserForm
    template_name = 'portals/login.html'

    def get_success_url(self):
        url = self.request.GET.get('next', '/')
        if 'addreply' in url:
            url = url.replace('addreply', 'discuss')
        return url

    def form_valid(self, form):
        user = authenticate(self.request, username=self.request.POST['username'], password=self.request.POST['password'])
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        form.add_error(None, "Invalid Username/Password")
        return super().form_invalid(form)


class LogOut(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

