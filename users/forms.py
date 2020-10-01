from django import forms
from . import models

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
        
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try: # user에 template에서 받아온 email을 담아 check_password()메서드 사용
            user = models.User.objects.get(email = email)
            if user.check_password(password):
                return self.cleaned_data    # 유저 존재, 패스워드 일치시
                # clean()을 썼다면 항상 cleaned_data를 리턴해 줘야 한다!!
            else:
                self.add_error("password",forms.ValidationError("Password is wrong"))
                # password is wrong 에러를 패스워드 쪽에만 뜨게 하려면 add_error()메서드 사용
                # raise forms.ValidationError("Password is wrong")
        except models.User.DoesNotExist:
            self.add_error("email",forms.ValidationError("User does not exist") )
            # raise forms.ValidationError("User does not exist")
            # 서로에게 depend(종속)되어 있음

# 두 개의 다른 field가 서로 관련이 있을 때 확인하는 method?
# ->cleaned_method

# clean method를 만들고 있다면 password만을 리턴하지 말고 
# 데이터 자체를 리턴해야 한다


# 정리
# clean이라고만 할 거면 error를 add_error를 사용해 직접 작성해 줘야 함
# clean_password(), clean_username() 이렇게 할 거면
# 그냥 error를 raise 하면 됨

# 맞는 건지 확인했고 정리된 데이터도 가짐
# 이제 유저를 로그인 시켜준다.