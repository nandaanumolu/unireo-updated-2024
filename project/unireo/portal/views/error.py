from django.shortcuts import render

def error_404(request, exception):
        data = {}
        return render(request,'error.html', data)

def error_500(request,  exception):
        data = {}
        return render(request,'error.html', data)
def error_403(request,  exception):
        data = {}
        return render(request,'error.html', data)
def error_400(request,  exception):
        data = {}
        return render(request,'error.html', data)