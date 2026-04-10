from django.db import models
# Create your models here.

class DepartmentCategory(models.Model):
    name=models.CharField(max_length=100, verbose_name="name")
    title = models.CharField(max_length=150, verbose_name='title', default='')
    text = models.TextField(help_text="text", verbose_name="desciption", default="Default about text")
    description = models.TextField(default='', verbose_name="description")
    text1 = models.TextField(help_text="text", verbose_name="desciption", default="Default about text")
    text2 = models.TextField(help_text="text", verbose_name="desciption", default="Default about text")
    text3 = models.TextField(help_text="text", verbose_name="desciption", default="Default about text")
    img=models.ImageField(upload_to='departments/',verbose_name="photo")
    def __str__(self):
        return self.name

class Department(models.Model):
    category = models.ForeignKey(DepartmentCategory, on_delete=models.CASCADE, related_name="departments", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Department Name", null=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Department Description", null=True)
    icon = models.CharField(max_length=50, blank=True, help_text="example: fas fa-heartbeat", null=True)
    doc_num = models.CharField(max_length=10,verbose_name="Doctor's number",default='')
    pro_num = models.CharField(max_length=10, verbose_name="Procedures number", default='')
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=100, verbose_name="name")
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='doctors',verbose_name="Department")
    specialty=models.CharField(max_length=100,verbose_name="specialty")
    image=models.ImageField(upload_to='doctors/',verbose_name='photo')
    experience_years = models.CharField(max_length=10, verbose_name="Experience years", default='')
    pro_num = models.CharField(max_length=10, verbose_name="Procedures number", default='')
    def __str__(self):
        return self.name

class Doctorpage(models.Model):
    name=models.CharField(max_length=100, verbose_name="name")
    title = models.CharField(max_length=150, verbose_name='title', default='')
    text = models.TextField(help_text="text", verbose_name="desciption", default="Default about text")
    description = models.TextField(default='', verbose_name="description")
    def __str__(self):
        return self.name

class Service(models.Model):
    title=models.CharField(max_length=150,verbose_name='title')
    description = models.TextField(default='',verbose_name="description")
    icon=models.CharField(max_length=50,help_text="example: bi bi-capsule",verbose_name="icon")
    image = models.ImageField(upload_to='service/', verbose_name='photo')
    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    def __str__(self):
        return self.question

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    def __str__(self):
        return self.name