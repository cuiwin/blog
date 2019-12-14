from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect("article:article_list")
            else:
                message = "账户或密码输入有误，请重新输入！"
        else:
            message = "账户或密码输入不合法！"
        return render(request, 'userprofile/login.html', {'message':message, 'login_form':user_login_form} )
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form':user_login_form}
        return render(request,'userprofile/login.html',context)
    else:
        return HttpResponse('请求方式不正确！')

def user_logout(request):
    logout(request)
    return redirect("article:index")