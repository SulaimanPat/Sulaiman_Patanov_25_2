from django.shortcuts import render, redirect
from users.usersForms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, DeleteView, DetailView

# Create your views here.

class RegisterSBV(ListView, CreateView):
    template_name = 'users/register.html'
    def get(self, request,*args, **kwargs):
        context = {
            'form': RegisterForm
        }
        return render(request, self.template_name, context=context)
    def post(self, request, **kwargs):
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get("password1") == form.cleaned_data.get('password2'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'Пароли не совпадают')
        return render(request, self.template_name, context={
            'form': form
        })

class loginSBV(ListView, CreateView):
    template_name = "users/login.html"
    def get(self, request, *args, **kwargs):
        context = {
            'form': LoginForm
        }

        return render(request, self.template_name, context=context)
    def post(self, request, **kwargs):
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            """authenticate"""
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            print(user)

            if user:
                """authorization"""
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error("username", "Пользователь не найден!")

        return render(request, self.template_name, context={
            "form": form
        })

def logout_view(request):
    logout(request)
    return redirect('/products')