from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='imgs/download.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image


'''
class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic= models.ImageField(null=True,blank=True, upload_to='images/profile/')
 
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        
        return reverse('homepage')
'''


