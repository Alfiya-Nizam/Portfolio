from .import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path('',views.index,name='index'),
    path('add_user_profile/', views.CreateProfile, name='add_user_profile'),
    path('profile/', views.profile_list, name='profile'),
    path('project_details/', views.project_details, name='project_details'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('add_education/', views.add_education, name='add_education'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
