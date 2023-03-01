from django.shortcuts import render,redirect

# Create your views here.
def show(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    return render(request,'api.html')
