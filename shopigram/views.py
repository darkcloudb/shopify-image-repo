from django.http.response import HttpResponseRedirect
from shopigram.forms import PostImg
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import View
from shopigram.models import Post
from shopigram.forms import LoginForm, SignUpForm, PostImg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class PostShow(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})


class PostImage(View):
    def get(self, request):
        form = PostImg()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = PostImg(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.create(
                image=data.get('image'),
                body=data.get('body'),
                author=request.user
            )
            return redirect(reverse('home', args=(post.id,)))
