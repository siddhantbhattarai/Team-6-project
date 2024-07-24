from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def privacy(request):
    return render(request, 'portfolio/privacy-policy.html')

def termsofservice(request):
    return render(request, 'portfolio/tos.html')

def teams(request):
    return render(request, 'portfolio/teams.html')

def careers(request):
    return render(request, 'portfolio/careers.html')


#Custom 404 Error
def custom_404(request, exception):
    return render(request, '404.html', status=404)