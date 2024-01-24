from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Blogs
class BlogListView(LoginRequiredMixin, ListView):
    model = Blogs
    template_name = 'blog_list.html'
    login_url = 'login'

class BlogDetailView(LoginRequiredMixin, DetailView): 
    model = Blogs
    template_name = 'blog_detail.html'
    login_url = 'login'

class BlogUpdateView(LoginRequiredMixin, UpdateView): 
    model = Blogs
    fields = ('title', 'body',)
    template_name = 'blog_edit.html'
    success_url = reverse_lazy('blog_list')
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blogs
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    template_name= 'blog_create.html'
    fields= ('title', 'body')
    success_url = reverse_lazy('blog_list')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)