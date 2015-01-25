from django.contrib import admin
from en.models import Company
from en.models import TeamMember
from en.models import Service
from en.models import Client
from en.models import StaticImages
from en.models import SliderImage
from en.models import SocialLinks
from en.models import StaticText


admin.site.register(Company)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(StaticImages)
admin.site.register(SliderImage)
admin.site.register(SocialLinks)
admin.site.register(StaticText)

