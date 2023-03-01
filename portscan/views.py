from django.shortcuts import render,redirect
import re,json,nmap3

# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        if cheak_ip(request.POST.get('ip').strip()):
            pass
        else:
            message = 'IP地址格式非法'
            return render(request,'port-scan.html',locals())
    return render(request,'port-scan.html')

def cheak_ip(string):
    ip_pattern = '(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    m = re.match(ip_pattern,string)
    if m != None:
        return True
    else:
        return False

def host_scan(host):
    nmap = nmap3.NmapHostDiscovery()
    result = nmap.nmap_portscan_only(host)

    return 
