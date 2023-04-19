from django.shortcuts import render,redirect
from api import models
# Create your views here.
def show(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    username = request.session['username']
    try:
        vt_key = models.APIs.objects.get(username=username).vt_key
    except models.APIs.DoesNotExist:
            message = '暂未添加API'
            return render(request,'api.html',locals())
    if request.method == 'POST':
        try:
            vt_key=request.POST.get('vt-key').strip()
        except models.APIs.DoesNotExist:
            message = '暂未添加API'
            return render(request,'api.html',locals())
        if not models.APIs.objects.filter(username=username):
            my_api = models.APIs()
            my_api.username = username
            my_api.vt_key = vt_key
            my_api.save()
        else:
            my_api = models.APIs.objects.get(username=username)
            my_api.vt_key = vt_key
            my_api.save()
    return render(request,'api.html',locals())


