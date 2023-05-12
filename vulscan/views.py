from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from vulscan import models
from api import models as api_models
import re,json,requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    vul_list = models.Vuls.objects.filter(username=request.session['username']).order_by("-datetime")
    vul_list = Paginator(vul_list, 7)
    page = request.GET.get('page')
    vul_list = vul_list.get_page(page)
    if request.method == 'POST':
        target = request.POST.get('url').strip()
        if check_url(target):
            pass
        else:
            message = 'URL格式非法'
            return render(request,'vul-scan.html',locals())
        try:
            api = api_models.APIs.objects.get(username=request.session['username']).av_key
        except api_models.APIs.DoesNotExist:
                message = '暂未添加API'
                return render(request,'vul-search.html',locals())
        headers = {
            'X-Auth': api,
            'Content-type': 'application/json'
        }
        awvs_host = "https://localhost:3443"
        api_url = awvs_host + '/api/v1/targets'
        data = {
            "address": target,
            "description": "AWVS API",
            "criticality": "10"
        }
        data_json = json.dumps(data)
        r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
        #获取target id
        target_id = r.json().get("target_id")
        print('target_id:', target_id)
        api_url = awvs_host + '/api/v1/scans'
        # 完全扫描："11111111-1111-1111-1111-111111111111"
        # 快速扫描："11111111-1111-1111-1111-111111111112"
        data = {
            "target_id": target_id,
            "profile_id": "11111111-1111-1111-1111-111111111112",
            "schedule":
            {
                "disable": False,
                "start_date": None,
                "time_sensitive": False
            }
        }
        #将字典data转化为json形式
        data_json = json.dumps(data)
        r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
        api_url = awvs_host + '/api/v1/scans'
        r = requests.get(url=api_url, headers=headers, verify=False)
        #获取scan_id
        scan_id = r.json().get("scans")[0].get("scan_id")
        #获取scan_session_id
        scan_session_id = r.json().get("scans")[0].get("current_session").get("scan_session_id")
        print(scan_session_id)
        api_url = awvs_host + '/api/v1/scans/' + str(scan_id) + '/results/'+ str(scan_session_id) + '/statistics'
        time = timezone.now()
        r = requests.get(url=api_url, headers=headers, verify=False)
        results = r.json()
        while(results['scanning_app']['wvs']['status'] == 'processing'):
            r = requests.get(url=api_url, headers=headers, verify=False)
            results = r.json()
        print(results)
        for i in results['scanning_app']['wvs']['main']['vulns']:
            print(i['name'],i['vuln_id'],i['severity'])
            new_result = models.Vuls()
            new_result.username = request.session['username']
            new_result.url =  target
            new_result.vul_id = i['vuln_id']
            new_result.vul = i['name']
            new_result.grade = int(i['severity'])
            new_result.datetime = time
            new_result.save() 
        return render(request,'vul-scan.html',locals())
    return render(request,'vul-scan.html',locals())   
def check_url(string):
    url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    m = re.match(url_pattern,string)
    if m != None:
        return True
    else:
        return False
