from django.contrib import admin

# Register your models here.
from .models import UserProfile,ProjectDetails,ExperienceDetails,EducationDetails
admin.site.register(UserProfile)
admin.site.register(ProjectDetails)
admin.site.register(ExperienceDetails)
admin.site.register(EducationDetails)

