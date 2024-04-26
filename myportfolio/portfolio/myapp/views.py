from django.shortcuts import render, redirect, get_object_or_404
from .models import Home, About, Skill, Project, Profile, Contact, Social
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import About
from .forms import AboutForm, HomeForm, SkillForm, ProjectForm, CvForm, SocialForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp:manage')
        else:
            # Invalid login, display an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'myapp/login.html')
    
def logout_view(request):
    logout(request)
    # Redirect to a success page or any other page after logout
    return redirect('myapp:login')  # Replace 'myapp:login' with the URL name of your login page

def portfolio(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    profile = Profile.objects.first()  
    home_image = Home.objects.first()
    about_section = About.objects.first()  
    skills = Skill.objects.all() 
    projects = Project.objects.all()
    social_links = Social.objects.first()

    context = {
        'home_image': home_image,
        'about_section': about_section,
        'skills': skills,
        'projects':projects,
        'profile': profile,
        'contact_form': contact_form, 
        'social_links':social_links,
    }
    return render(request, 'myapp/portfolio.html', context)

@login_required(login_url='/login')
def manage(request):
    homes = Home.objects.all()
    abouts = About.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    contacts = Contact.objects.all()
    profiles = Profile.objects.all()
    socials = Social.objects.all()

    context = {
        'homes': homes,
        'abouts': abouts,
        'skills': skills,
        'projects': projects,
        'contacts': contacts,
        'profiles': profiles,
        'socials': socials,
    }
    return render(request, 'myapp/manage.html', context)

@login_required(login_url='/login')
def about_create(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:manage')
    else:
        form = AboutForm()
    return render(request, 'myapp/about.html', {'form': form})

@login_required(login_url='/login')
def about_edit(request, pk):
    item = get_object_or_404(About, pk=pk)
    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = AboutForm(instance=item)
    return render(request, 'myapp/about.html', {'form': form})


@login_required(login_url='/login')
def home_edit(request, pk):
    item = get_object_or_404(Home, pk=pk)
    if request.method == "POST":
        form = HomeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
        
    else:
        form = HomeForm(instance=item)
    return render(request, 'myapp/home.html', {'form': form})

@login_required(login_url='/login')
def skill_edit(request, pk):
    item = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST,  request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = SkillForm(instance=item)
    return render(request, 'myapp/skill.html', {'form': form})

@login_required(login_url='/login')
def portfolio_edit(request, pk):
    item = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST,  request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = ProjectForm(instance=item)
    return render(request, 'myapp/projects.html', {'form': form})

@login_required(login_url='/login')
def delete_skill(request, pk):        
    skill = Skill.objects.get(pk=pk)
    skill.delete()

    return redirect('myapp:manage' )   

@login_required(login_url='/login')
def delete_project(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        # Handle the case where the project doesn't exist
        # For example, you can show an error message or redirect to a different page
        return HttpResponse("Project not found", status=404)
    
    project.delete()
    return redirect('myapp:manage') 

@login_required(login_url='/login')
def delete_contact(request, pk):        
    contact = Contact.objects.get(pk=pk)
    contact.delete()

    return redirect('myapp:manage' )   

@login_required(login_url='/login')
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = SkillForm()
    
    return render(request, 'myapp/skill.html', {'form': form})

@login_required(login_url='/login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = ProjectForm()
    
    return render(request, 'myapp/projects.html', {'form': form})

@login_required(login_url='/login')
def cv_edit(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = CvForm(request.POST,  request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = CvForm(instance=item)
    return render(request, 'myapp/profile.html', {'form': form})

@login_required(login_url='/login')
def social_edit(request, pk):
    item = get_object_or_404(Social, pk=pk)
    if request.method == "POST":
        form = SocialForm(request.POST,  request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')  # Render a template to close the window
    else:
        form = SocialForm(instance=item)
    return render(request, 'myapp/social.html', {'form': form})