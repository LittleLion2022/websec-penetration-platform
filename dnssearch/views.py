from django.shortcuts import render,redirect
import re,requests
# Create your views here.
def scanner(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        pass
    return render(request,'dns-search.html')

def check_domin():
    pass