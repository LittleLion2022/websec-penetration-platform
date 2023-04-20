from django.shortcuts import render,redirect
from api import models
# Create your views here.
def show(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    username = request.session['username']
    # print(username)
    if request.method == 'POST':
        try:
            vt_key=request.POST.get('vt-key').strip()
        except models.APIs.DoesNotExist:
            message = '暂未添加Virus Total API'
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
        
        try:
            av_key=request.POST.get('av-key').strip()
        except models.APIs.DoesNotExist:
            message = '暂未添加AWVS API'
            return render(request,'api.html',locals())
        if not models.APIs.objects.filter(username=username):
            my_api = models.APIs()
            my_api.username = username
            my_api.av_key = av_key
            my_api.save()
        else:
            my_api = models.APIs.objects.get(username=username)
            my_api.av_key = av_key
            my_api.save()

        try:
            ze_key=request.POST.get('ze-key').strip()
        except models.APIs.DoesNotExist:
            message = '暂未添加Zoomeye API'
            return render(request,'api.html',locals())
        if not models.APIs.objects.filter(username=username):
            my_api = models.APIs()
            my_api.username = username
            my_api.ze_key = ze_key
            my_api.save()
        else:
            my_api = models.APIs.objects.get(username=username)
            my_api.ze_key = ze_key
            my_api.save()

    try:
        vt_key = models.APIs.objects.get(username=username).vt_key
    except models.APIs.DoesNotExist:
            message = '暂未添加Virus Total API'
            return render(request,'api.html',locals())
    try:
        av_key = models.APIs.objects.get(username=username).av_key
    except models.APIs.DoesNotExist:
            message = '暂未添加AWVS API'
            return render(request,'api.html',locals())
    try:
        ze_key = models.APIs.objects.get(username=username).ze_key
    except models.APIs.DoesNotExist:
            message = '暂未添加Zoomeye API'
            return render(request,'api.html',locals())
    return render(request,'api.html',locals())


