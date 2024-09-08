from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import PostJob, Application, Register

# Create your views here.
##### LANDING PAGE #####
def Home(request):
    return render(request, 'lance/home.html')

##### SIGN UP #####
def SignUp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))

        user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()

    page = 'signup'
    context = {
        'page': page,
    }
    return render(request, 'lance/signup_login.html', context)

##### LOG IN #####
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client-dashboard')
        else:
            return redirect('login')

    page = 'login'
    context = {
        'page': page,
    }
    return render(request, 'lance/signup_login.html', context)

##### LOG OUT #####
def LogOut(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        logout(user)
        return redirect('home')
    page = 'logout'
    context = {
        'page': page,
    }
    return render(request, 'lance/signup_login.html', context)

##### TALENT #####
def TalentDashboard(request):
    page = 'talent_page'
    jobs = PostJob.objects.all()
    context = {
        'page': page,
        'jobs': jobs
    }
    return render(request, 'lance/dashboard.html', context)

def TalentJobs(request):
    if request.method == 'POST':
        job_info = request.POST['job_info']
        bid = request.POST['bid']
        cover_letter = request.POST['cover_letter']
        applicant_name = request.POST['applicant_name']
        author = request.POST['author']

        applications = Application.objects.create(job_title=job_info, bid=bid, cover_letter=cover_letter, applicant_name=applicant_name, job_author=author)
        

    page = 'jobs'
    jobs = PostJob.objects.all()
    context = {
        'page': page,
        'jobs': jobs
    }
    return render(request, 'lance/talent.html', context)

def TalentApplications(request):
    application = Application.objects.filter(applicant_name=request.user)

    jobs = PostJob.objects.all()
    page = 'applications'
    context = {
        'jobs': jobs,
        'page': page,
        'applications': application,
    }
    return render(request, 'lance/talent.html', context)

def TalentProfile(request):
    page = 'profile'
    context = {
        'page': page,
    }
    return render(request, 'lance/talent.html', context)

def TalentHires(request):
    page = 'hires'
    context = {
        'page': page,
    }
    return render(request, 'lance/talent.html', context)

##### CLIENT #####
def ClientDashboard(request):
    jobs = PostJob.objects.filter(author=request.user)
    number_of_jobs = len(jobs)
    print(len(jobs))
    page = 'client_page'
    context = {
        'page': page,
        'number_of_jobs': number_of_jobs
    }
    return render(request, 'lance/dashboard.html', context)

def ClientProfile(request):
    try:
        user_profile = User.objects.get(username=request.user)
        profile_data = Register.objects.get(user=request.user)
    except:
        pass
    page = 'profile'
    context = {
        'page': page,
        'user': user_profile,
        'profile_data': profile_data
    }
    return render(request, 'lance/client.html', context)

def ClientProfileUpdate(request):
    if request.method == "PUT":
        username = request.PUT['username']
        firstname = request.PUT['firstname']
        lastname = request.PUT['lastname']
        email = request.PUT['email']
        img = request.PUT['img']
        #print(username, fistname, lastname, email, img)
    page = 'client_update'
    context = {
        'page': page,
    }
    return render(request, 'lance/talent.html', context)

def ClientApplications(request):
    applications = Application.objects.filter(job_author=request.user.first_name)
    print(len(applications))

    page = 'applications'
    context = {
        'page': page,
        'applications': applications,
    }
    return render(request, 'lance/client.html', context)

def ClientJobs(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_budget = request.POST.get('budget')
        
        new_job = PostJob.objects.create(title=job_title, description=job_description, budget=job_budget, author=request.user)

    jobs = PostJob.objects.filter(author=request.user)
    print(len(jobs))
    page = 'jobs'
    context = {
        'page': page,
        'jobs': jobs,
    }
    return render(request, 'lance/client.html', context)

def ClientHires(request):
    page = 'hires'
    context = {
        'page': page,
    }
    return render(request, 'lance/client.html', context)
