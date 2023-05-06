from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from vulsearch import models
from api import models as api_models
import zoomeye.sdk as zoomeye
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    record_list = models.Records.objects.filter(username=request.session['username']).order_by("-datetime")
    record_list = Paginator(record_list, 7)
    page = request.GET.get('page')
    record_list = record_list.get_page(page)
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword == '':
            message = '目标为空'
            return render(request,'vul-search.html',locals())   
        try:
            api = api_models.APIs.objects.get(username=request.session['username']).ze_key
        except api_models.APIs.DoesNotExist:
                message = '暂未添加API'
                return render(request,'vul-search.html',locals())
        zm = zoomeye.ZoomEye(api_key = str(api))
        print(zm.resources_info())
        zm.dork_search(keyword)
        results = zm.dork_filter('app,ip,country,city')
        time =timezone.now()
        for result in results:
            new_result = models.Records()
            new_result.username = request.session['username']
            new_result.datetime = time
            new_result.keyword = keyword
            new_result.app = result[0]
            new_result.ip = result[1]
            new_result.country = result[2]
            new_result.city = result[3]
            new_result.save()    
    return render(request,'vul-search.html',locals())