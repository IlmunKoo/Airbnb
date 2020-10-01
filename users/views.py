from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home") # 여기로 가서 실제 url을 줌, form을 가져올 때 url은 아직 불려지지 않음 
    # reverse_lazy : 자동으로 url을 호출하는 것이 아니라 필요할 때 url을 호출하는 것
    # lazy: 바로 실행되는 것이 아니라 필요할 때 실행되는 것임

    # 로그인 정보가 유효한지
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username = email, password = password )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
        # success_url로 가서 다시 작동한다

  
# 아래 function 기반 view 하는 것과 같은 것 하는 중
# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))