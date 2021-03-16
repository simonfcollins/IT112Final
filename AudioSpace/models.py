from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# parent thread
class Forum(models.Model):
    userID = models.ForeignKey(User, null = True, on_delete = models.DO_NOTHING)
    topic= models.CharField(max_length=300)
    description = models.TextField(blank=True)
    refLinks = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.topic)

    class Meta:
        db_table = 'Forum'
        verbose_name_plural = 'Forums'
 

# child thread
class Discussion(models.Model):
    userID = models.ForeignKey(User, null = True, on_delete = models.DO_NOTHING)
    forum = models.ForeignKey(Forum, blank=True,on_delete=models.CASCADE)
    discuss = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

 
    def __str__(self):
        return str(self.forum)
    
    class Meta:
        db_table = 'Discussion'
        verbose_name_plural = 'Discussions'


class Review(models.Model):
    revTitle = models.CharField(max_length = 255)
    userID = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    datePosted = models.DateField(auto_now_add=True,null=True)
    rating = models.IntegerField(default = 0, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    revText = models.TextField()
    
    def __str__(self):
        return self.revTitle

    class Meta:
        db_table = 'Review'
        verbose_name_plural = 'Reviews'

# Create your models here.
