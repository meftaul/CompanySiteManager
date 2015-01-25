from django.contrib import admin
from ger.models import Company
from ger.models import TeamMember
from ger.models import Service
from ger.models import Client
from ger.models import StaticImages
from ger.models import SliderImage
from ger.models import SocialLinks
from ger.models import StaticText


admin.site.register(Company)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(StaticImages)
admin.site.register(SliderImage)
admin.site.register(SocialLinks)
admin.site.register(StaticText)

