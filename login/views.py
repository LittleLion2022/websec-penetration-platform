from django.shortcuts import render,redirect
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
            message = '用户名不存在或密码错误' 
            return render(request,'login.html',locals())

    if not request.session.get('is_login', None):
        return redirect('/')
    return render(request,'index.html',locals())

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
    if not request.session.get('is_login', None):
        return redirect('/')
    current_user = request.session['username']
    if request.method == 'POST':
        oldpassword = request.POST.get('oldpassword')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_obj = models.User.objects.filter(username=current_user,password=hash_password(oldpassword)).first()
        if user_obj:
            if not password1 and not password2:
                message = '密码不能为空' 
                return render(request, 'change-password.html', locals())
            if oldpassword == password1 or oldpassword == password2:
                message = '新的密码不能与旧的密码一致'
                return render(request, 'change-password.html',locals())
            if password1 == password2:
                user = models.User.objects.get(username=current_user)
                user.password = hash_password(password1)
                user.save()
                request.session.flush()
                return redirect("/")
            else:
                message='两次输入密码不一致'
                return render(request, 'change-password.html',locals())
        else:
            message = '密码错误，详情请联系管理员'
            return render(request, 'change-password.html',locals())
    return render(request,'change-password.html',locals())
