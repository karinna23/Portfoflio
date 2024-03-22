from django import forms
from .models import Contact, About, Home, Skill, Project, Profile, Social

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'project_name']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['aboutme', 'image1', 'image2']

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['image']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'logo', 'percentage']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class CvForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cv_image', 'cv_file']

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['fblink', 'instalink', 'xlink', 'tglink']
