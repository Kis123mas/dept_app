# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentGroup, Course, Seminar, Notification, BestStudent, Profile

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['lecturer', 'message']


class BestStudentForm(forms.ModelForm):
    class Meta:
        model = BestStudent
        fields = ['lecturer', 'grade', 'name', 'course', 'picture']


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_lecturer', 'course_code', 'course_title', 'pdf_file']

    def __init__(self, *args, **kwargs):
        # Get the user from the kwargs
        user = kwargs.pop('user', None)

        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

        # Set the initial value for the course_lecturer field
        if user:
            self.fields['course_lecturer'].initial = user

class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ['lecturer', 'title', 'link', 'pdf_file']

class CreateUserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=StudentGroup.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your username',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your email address',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your password',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Confirm your password',
        })
        self.fields["group"].widget.attrs.update({
            'required':'',
            'class':'form-control',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["profile_pic"].widget.attrs.update({
            'class':'btn btn-primary btn-sm',
            'title':'Upload new profile image',
            'class':'bi bi-upload',
            'name':'profile_pic'
        })
        self.fields["mat_no"].widget.attrs.update({
            'required':'',
            'name': 'mat_no',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["firstname"].widget.attrs.update({
            'required':'',
            'name': 'firtname',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["middlename"].widget.attrs.update({
            'required':'',
            'name': 'middlename',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["lastname"].widget.attrs.update({
            'required':'',
            'name': 'lastname',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["phone"].widget.attrs.update({
            'required':'',
            'name': 'phone',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name': 'email',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["address"].widget.attrs.update({
            'required':'',
            'name': 'address',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["state"].widget.attrs.update({
            'required':'',
            'name': 'state',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["country"].widget.attrs.update({
            'required':'',
            'name': 'country',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["level"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-select',
            'id':'fullName'
        })
        self.fields["twitter_profile"].widget.attrs.update({
            'required':'',
            'name': 'twitter_profile',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["facebook_profile"].widget.attrs.update({
            'required':'',
            'name': 'facebook_profile',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["instagram_profile"].widget.attrs.update({
            'required':'',
            'name': 'instagram_profile',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']