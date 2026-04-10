from django.db import models

class Home(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(help_text="text",verbose_name="desciption")
    image=models.ImageField(upload_to="home/")
    def __str__(self):
        return self.title
class About(models.Model):
    title1=models.CharField(max_length=200,verbose_name="title")
    text = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    title2= models.CharField(max_length=200, verbose_name="title",default="Default about text")
    text1 = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    text2 = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    text3 = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    text4 = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    text5 = models.TextField(help_text="text", verbose_name="desciption",default="Default about text")
    image1 = models.ImageField(upload_to="about/")
    image2 = models.ImageField(upload_to="about/")
    image3 = models.ImageField(upload_to="about/")
# Create your models here.
