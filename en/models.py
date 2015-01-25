from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='company')
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team_members')
    linkedin = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    links = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class StaticImages(models.Model):
    home_who_we_are = models.ImageField(upload_to='home')
    home_our_advantages = models.ImageField(upload_to='home')
    contact_display_img = models.ImageField(upload_to='contact')


class SliderImage(models.Model):
    label = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='slider_images')

    def __str__(self):
        return self.label


class SocialLinks(models.Model):
    site_name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.site_name
    

class StaticText(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.heading

    