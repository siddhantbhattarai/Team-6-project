from django.shortcuts import render
from portfolio.models import GeneralInfo
# Create your views here.
def index(request):
    
    general_info = GeneralInfo.objects.all()
    
    context = {
        'company_name': 'general_info.company_name',
        'company_logo': 'general_info.company_logo',
        'company_address': 'general_info.company_address',
        'company_phone': 'general_info.company_phone',
        'company_email': 'general_info.company_email',
        'company_website': 'general_info.company_website',
        'company_facebook': 'general_info.company_facebook',
        'company_twitter': 'general_info.company_twitter',
        'company_linkedin': 'general_info.company_linkedin',
        'company_instagram': 'general_info.company_instagram',
        'company_youtube': 'general_info.company_youtube',
        'company_tiktok': 'general_info.company_tiktok',
        'company_about': 'general_info.company_about',
        'company_mission': 'general_info.company_mission',
        'company_vision': 'general_info.company_vision',
    }
    
    return render(request, 'index.html', context)