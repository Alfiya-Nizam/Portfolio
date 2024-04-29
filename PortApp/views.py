from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile,ProjectDetails,ExperienceDetails,EducationDetails

# Create your views here.
def index(request):
    return render(request,'index.html')
def CreateProfile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')  # Update the key to 'gender'
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        work_experience = request.POST.get('work_experience')
        certifications = request.POST.get('certifications')
        accomplishments = request.POST.get('accomplishments')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        image = request.FILES.get('image')
  
        profile = UserProfile.objects.create(
            name=name,
            age=age,
            gender=gender,
            location=location,
            skills=skills,
            education=education,
            work_experience=work_experience,
            certifications=certifications,
            accomplishments=accomplishments,
            email=email,
            phone_number=phone_number,
            image=image
        )
     
    return render(request, 'add_user_profile.html')  

def profile_list(request):
    profiles = UserProfile.objects.all()
    projects =ProjectDetails.objects.all()
    experience = ExperienceDetails.objects.all()
    education = EducationDetails.objects.all()
    return render(request, 'profile.html', {'profiles': profiles,'projects':projects,'experience':experience,'education':education})

def project_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        project = ProjectDetails.objects.create(
            name=name,
            description=description
        )
    return render(request, 'project_details.html')  

def add_experience(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        description = request.POST.get('description')

        project = ExperienceDetails.objects.create(
            name=name,
            location=location,
            sdate=sdate,
            edate=edate,
            description=description
        )
    return render(request, 'add_experience.html') 

def add_education(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        university = request.POST.get('university')
        mark = request.POST.get('mark')

        project = EducationDetails.objects.create(
            name=name,
            sdate=sdate,
            edate=edate,
            university=university,
            mark=mark
        )
    return render(request, 'add_education.html') 