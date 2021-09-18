from django.http.response import HttpResponse
from shopigram.forms import PostImg
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from shopigram.models import Post
from django.contrib.auth.models import User
from shopigram.forms import LoginForm, SignUpForm, PostImg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class PostShow(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'index.html', {'posts': posts})


class PostImage(LoginRequiredMixin, View):
    def get(self, request):
        form = PostImg()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = PostImg(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(
                    image=data['image'],
                    body=data['body'],
                    author=request.user
                    )
                return redirect(reverse("home"))
        return render(request, 'generic_form.html', {'form': form})


class PostDetail( LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        return render(request, 'post_detail.html', {'post': post})


class DeletePost( LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        post = Post.objects.get(id=post_id)
        if request.user.is_staff or request.user == post.author:
            post.delete()
            return redirect(reverse('home'))
        else:
            return HttpResponse("Access Denied - Need staff/admin permissions")


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

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
