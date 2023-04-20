from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from dnssearch import models
from api import models as api_models
import re,json,requests
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    domain_list = models.Domains.objects.filter(username=request.session['username']).order_by("-datetime")
    domain_list = Paginator(domain_list, 7)
    page = request.GET.get('page')
    domain_list = domain_list.get_page(page)
    if request.method == 'POST':
        domain = request.POST.get('domain').strip()
        try:
            limit = int(request.POST.get('limit').strip())
        except ValueError:
            message = '请输入显示条数'
            return render(request,'dns-search.html',locals())
        print(limit)
        if check_domain(domain):
            if limit <= 0:
                limit = 12
            url = f'https://www.virustotal.com/api/v3/domains/{domain}/subdomains?limit={limit}'
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
            result = json.loads(response.text)
            if  response.status_code == 200:
                time = time = timezone.now()
                count = int(result['meta']['count'])
                for result in result['data']:
                    print(result['id'])
                    new_result = models.Domains()
                    new_result.username = request.session['username']
                    new_result.domain = domain
                    new_result.subdomain = result['id']
                    new_result.count = count
                    new_result.datetime = time
                    new_result.save()
            else:
                message = result["error"]["message"]
                return render(request,'dns-search.html',locals())
        else:
            message = '域名格式非法'
            return render(request,'dns-search.html',locals())
    return render(request,'dns-search.html',locals())

def check_domain(string):
    domain_pattern = '(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    m = re.match(domain_pattern,string)
    if m != None:
        return True
    else:
        return False