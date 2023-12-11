# models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    course_code= models.CharField(max_length=255)
    associated_lectutrers = models.CharField(max_length=255)
    credit_load = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploaded_pdfs/')

    def __str__(self):
        return str(self.course_lecturer)


class Notification(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    def __str__(self):
        return str(self.message)

class BestStudent(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='best_student_pics/')

    def __str__(self):
        return str(self.name)
    
class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='lecturer/')

    def __str__(self):
        return str(self.name)
    
class AdministrativeStaff(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='lecturer/')

    def __str__(self):
        return str(self.name)

class Technical(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='lecturer/')

    def __str__(self):
        return str(self.name)


class Seminar(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploaded_pdfs/')

    def __str__(self):
        return str(self.title)

class StudentGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    LEVEL = (
        ('100', '100'), 
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('alumni', 'alumni'),
        ('lecturer', 'lecturer'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile2.png", null=True)
    mat_no = models.CharField(max_length=200, null=True, blank=True)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    twitter_profile = models.CharField(max_length=200, null=True, blank=True)
    facebook_profile = models.CharField(max_length=200, null=True, blank=True)
    instagram_profile = models.CharField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=200, null=True, choices=LEVEL, blank=True) 
    date_created = models.DateTimeField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.firstname) + ' | ' + str(self.level)
    


