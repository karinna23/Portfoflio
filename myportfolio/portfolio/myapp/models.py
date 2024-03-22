from django.db import models

class Home(models.Model):
    image = models.ImageField(upload_to='files/')

    def __str__(self):
        return f"image {self.pk}"
    
class About(models.Model):
    aboutme = models.TextField()
    image1 = models.ImageField(upload_to='files/')
    image2 = models.ImageField(upload_to='files/')
    
    def __str__(self):
        return "About Section"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='files/')
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='files/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.project_name}"

class Profile(models.Model):
    cv_image = models.ImageField(upload_to='files/', null=True, blank=True)
    cv_file = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return f"Profile {self.pk}"

class Social(models.Model):
    fblink = models.URLField(max_length=200)
    instalink = models.URLField(max_length=200)
    xlink = models.URLField(max_length=200)
    tglink = models.URLField(max_length=200)

    def get_urls(self):
        # Return a dictionary of the links
        return {
            'facebook': self.fblink,
            'instagram': self.instalink,
            'x_link': self.xlink,
            'telegram': self.tglink,
        }





