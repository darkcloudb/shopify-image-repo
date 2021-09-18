from django.http.response import HttpResponseRedirect
from shopigram.forms import PostImg
from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import View
from shopigram.models import Post
from django.contrib.auth.models import User
from shopigram.forms import LoginForm, SignUpForm, PostImg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class PostShow(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
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
        return render(request, 'generic_form.html', {'form': form})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            login(request, user)
            return redirect(reverse('home'))


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data.get('username'),
                password=data.get('password')
            )
            if user:
                login(request, user)
                return redirect(request.GET.get("next", '/'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
