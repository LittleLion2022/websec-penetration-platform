from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from dirscan import models
import re,requests
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    url_list = models.Dirs.objects.filter(username=request.session['username']).order_by("-datetime")
    url_list = Paginator(url_list, 7)
    page = request.GET.get('page')
    url_list = url_list.get_page(page)
    if request.method == 'POST':
        if check_url(request.POST.get('url').strip()):
            target = request.POST.get('url').strip()
            time = timezone.now()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
            }
            with open('./dirscan/dicts/dict.txt','r') as f:
                dir_list = f.readlines()
                for dir in dir_list:
                    new_result = models.Dirs()
                    response = requests.get(url=target+'/'+dir,headers=headers)
                    new_result.username =  request.session['username']
                    new_result.url = target
                    new_result.dir = dir
                    new_result.httpcode = response.status_code
                    new_result.datetime = time
                    new_result.save()
        else:
            message = 'URL格式非法'
            return render(request,'dir-scan.html',locals())
    return render(request,'dir-scan.html',locals())

def check_url(string):
    url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    m = re.match(url_pattern,string)
    if m != None:
        return True
    else:
        return False
