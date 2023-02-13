from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from login import models
import hashlib
# Create your views here.
def index(request):
    if request.method == 'POST':
        username=request.POST.get('username').strip()
        password=request.POST.get('password')
        user_obj = models.User.objects.filter(username=username,password=hash_password(password)).first()
        if user_obj:
            request.session['is_login'] = True
            request.session['username'] = user_obj.username
            return redirect('/index/')
        else:
            return redirect('/')
    if not request.session.get('is_login', None):
        return redirect('/')
    return render(request,'index.html',{'login_user':request.session['username']})

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not username:
            message = '用户名不能为空' 
            return render(request, 'register.html', locals())
        if not password1 and not password2:
            message = '密码不能为空' 
            return render(request, 'register.html', locals())
        if password1 != password2:
            message = '两次输入密码不一致'
            return render(request, 'register.html', locals())
        else:
            samename = models.User.objects.filter(username=username)
            if samename:
                message = '用户名'+username+'已经存在'
                return render(request, 'register.html', locals())
            new_user = models.User()
            new_user.username = username
            new_user.password = hash_password(password1)
            new_user.save()
            return render(request, 'register.html', locals())
    return render(request,'register.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/")
    request.session.flush()
    return redirect("/")

def hash_password(password,salt='websec-salt123'):
    sha256 = hashlib.sha256()
    password += salt
    sha256.update(password.encode())
    return sha256.hexdigest()

def change_password(request):
    pass
    return render(request,'change-password.html',{'login_user':request.session['username']})