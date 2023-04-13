from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from portscan import models
import re,nmap3

# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    port_list = models.Ports.objects.filter(username=request.session['username']).order_by("-datetime")
    port_list = Paginator(port_list, 7)
    page = request.GET.get('page')
    port_list = port_list.get_page(page)
    if request.method == 'POST':
        if check_ip(request.POST.get('ip').strip()):
            host = request.POST.get('ip').strip()
            results,time =  host_scan(host)
            for result in results:
                new_result = models.Ports()
                new_result.username = request.session['username']
                new_result.ip = host
                new_result.portid = result['portid']
                new_result.service = result['service']['name']
                new_result.datetime = time
                new_result.save()
        else:
            message = 'IP地址格式非法'
            return render(request,'port-scan.html',locals())
    
    return render(request,'port-scan.html',locals())

def check_ip(string):
    ip_pattern = '(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    m = re.match(ip_pattern,string)
    if m != None:
        return True
    else:
        return False

def host_scan(host):
    nmap = nmap3.NmapHostDiscovery()
    result = nmap.nmap_portscan_only(host)
    ports = result[host]['ports']
    time = timezone.now()
    for i in ports:
        print(f'{i["protocol"]}\t{i["portid"]}\t{i["state"]}\t{i["service"]["name"]}')
    return ports,time
