from django.shortcuts import render

from ger.models import TeamMember
from ger.models import Service
from ger.models import Client
from ger.models import SliderImage
from ger.models import SocialLinks
from ger.models import StaticImages
from ger.models import Company
from ger.models import StaticText


def home(request):
    static_text = StaticText.objects.all()
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    slider_images = SliderImage.objects.all()
    static_images = StaticImages.objects.all()
    
    context = { 'slider_images' : slider_images, 'services' : services,
               'social_links': social_links, 'static_images':static_images,
               'company':comapny, 'static_text' : static_text}
    return render(request, 'ger_home.html', context)


def clients(request):
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    clients_list = Client.objects.all()
    context = { 'clients_list': clients_list, 'services' : services,
               'social_links': social_links, 'company':comapny }
    return render(request, 'ger_clients.html', context)


def contact(request):
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    context = {'services' : services, 'social_links': social_links, 'company':comapny }
    return render(request, 'ger_contact.html', context)


def about(request):
    static_text = StaticText.objects.all()
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    members_list = TeamMember.objects.all()
    context = {'members_list':members_list, 'services' : services,
               'social_links': social_links, 'company':comapny,'static_text' : static_text}

    return render(request, 'ger_about.html', context)


def detail(request, member_id):
    comapny = Company.objects.all()
    static_text = StaticText.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    member = TeamMember.objects.get(id=member_id)
    context = { 'member' : member, 'services' : services, 'static_text' : static_text,
               'social_links': social_links, 'company':comapny}
    return render(request, 'ger_detail.html', context)


def service(request, service_id):
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    
    service = Service.objects.get(id=service_id)
    context = { 'service' : service, 'services' : services,
               'social_links': social_links,'company':comapny}
    return render(request, 'ger_service.html', context)


def advantage(request):
    static_text = StaticText.objects.all()
    comapny = Company.objects.all()
    services = Service.objects.all()
    social_links = SocialLinks.objects.all()
    
    context = {'services' : services,
               'social_links': social_links,
               'company':comapny, 'static_text' : static_text}
    return render(request, 'ger_advantage.html', context)


