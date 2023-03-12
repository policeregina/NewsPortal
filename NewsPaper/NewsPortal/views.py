from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Category, SubscribersCAT, User, PostCategory
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'newslist.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'sel_news'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'PT'
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'AR'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'PT'
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'AR'
        return super().form_valid(form)


class NewsDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news_list')


class CategoryList(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    paginate_by = 10


class SelCatList(ListView):
    model = Post
    template_name = 'politicalNews.html'
    context_object_name = 'SelCatPosts'
    paginate_by = 20


@login_required
def subscribe_political(request):
    user = request.user
    if not SubscribersCAT.objects.filter(rel_cat_id=2, rel_user_id=user.id):
        SubscribersCAT.objects.create(rel_cat_id=2, rel_user_id=user.id)
    return redirect('http://127.0.0.1:8000/categories/politics/')


@login_required
def subscribe_education(request):
    user = request.user
    if not SubscribersCAT.objects.filter(rel_cat_id=4, rel_user_id=user.id):
        SubscribersCAT.objects.create(rel_cat_id=4, rel_user_id=user.id)
    return redirect('http://127.0.0.1:8000/categories/education/')


@login_required
def subscribe_sport(request):
    user = request.user
    if not SubscribersCAT.objects.filter(rel_cat_id=1, rel_user_id=user.id):
        SubscribersCAT.objects.create(rel_cat_id=1, rel_user_id=user.id)
    return redirect('http://127.0.0.1:8000/categories/sport')


@login_required
def subscribe_health(request):
    user = request.user
    if not SubscribersCAT.objects.filter(rel_cat_id=3, rel_user_id=user.id):
        SubscribersCAT.objects.create(rel_cat_id=3, rel_user_id=user.id)
    return redirect('http://127.0.0.1:8000/categories/health/')



