from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from dnssearch import models
from api import models as api_models
import re,requests
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        domain = request.POST.get('domain').strip()
        if check_domain(domain):
            url = f'https://www.virustotal.com/api/v3/domains/{domain}/subdomains?limit=12'
            try:
                api = api_models.APIs.objects.get(username=request.session['username']).vt_key
            except api_models.APIs.DoesNotExist:
                message = '暂未添加API'
                return render(request,'dns-search.html',locals())
            headers = {
                "accept": "application/json",
                "x-apikey": api
            }
            response = requests.get(url,headers=headers)
            print(response.text)
            print(headers['x-apikey'])
        else:
            message = '域名格式非法'
            return render(request,'dns-search.html',locals())
    return render(request,'dns-search.html')

def check_domain(string):
    domain_pattern = '(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    m = re.match(domain_pattern,string)
    if m != None:
        return True
    else:
        return False