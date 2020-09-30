from django.views import View
from django.shortcuts import render


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "users/Login.html")

    def post(self, request):
        pass

# 아래 function 기반 view 하는 것과 같은 것 하는 중
# def login_view(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         pass