from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

##category
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

#neighborhood
class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    securityline = models.IntegerField(null=True, blank=True)
    hospitalhelpline = models.IntegerField(null=True, blank=True)
    occupants = models.IntegerField(default=0, null=True)

    def __str__(self):
      return self.name

    def create_neighborhood(self):
      self.save()

    @classmethod
    def delete_neighborhood(cls, id):
      cls.objects.filter(id=id).delete()

    @classmethod
    def find_neighborhood(cls, searchterm):
      searchresults = cls.objects.filter(name__icontains=searchterm)
      return searchresults

    @classmethod
    def update_neighborhood(cls, id, name):
      cls.objects.filter(id=id).update(name=name)  
      
#profile    
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    phone = models.IntegerField(null=True, blank=True)
    profile_photo = CloudinaryField('image')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
      return self.username 

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
      if created:
        Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

    

#business 
class Business(models.Model):
    businessname = models.CharField(max_length=200)
    description = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
      return self.businessname

    def save_business(self):
      self.save()

    @classmethod
    def delete_business(cls, id): 
      cls.objects.filter(id=id).delete()

    @classmethod
    def searchbusiness(cls, searchterm):
      searchresults = cls.objects.filter(businessname__icontains = searchterm)
      return searchresults  

  
class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    story = models.TextField()
    timeuploaded = models.DateTimeField(auto_now_add=True)
    postuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
      return self.title

    def save_post(self):
      self.save()

    @classmethod
    def delete_post(cls, id):
      cls.objects.filter(id=id).delete() 