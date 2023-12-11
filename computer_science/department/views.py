from pyexpat.errors import messages  # Importing messages from an incorrect module, this line seems unnecessary

from django.shortcuts import render, redirect
from .forms import CreateUserForm, PDFUploadForm, SeminarForm, NotificationForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentGroup, Course, Seminar, Notification, BestStudent, Profile, Lecturer, AdministrativeStaff, Technical
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def registerStudent(request):
    """
    View for registering a student.
    """
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get the selected group from the form
            group = form.cleaned_data['group']

            # Create or get the student group
            student_group, created = Group.objects.get_or_create(name=group)

            # Assign the user to the student group
            user.groups.add(student_group)

            return redirect('login')  # Redirect to login page or any other page
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'NiceAdmin/registerstudent.html', context)


def loginPage(request):
    """
    View for handling user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)  # Session expires when the browser is closed
            return redirect('dashboard')  # Redirect to the dashboard or any other page after login
        else:
            messages.error(request, 'Invalid username or password.')

    context = {}
    return render(request, 'NiceAdmin/pages-login.html', context)


def logoutPage(request):
    """
    View for handling user logout.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def home(request):
    """
    Home view.
    """
    context = {}
    return render(request, 'department/index.html', context)


def profilePage(request):
    """
    View for displaying and updating user profile.
    """
    user = request.user

    # Check if the user already has a profile
    if hasattr(user, 'profile'):
        form = ProfileForm(request.POST or None, request.FILES or None, instance=user.profile)
    else:
        form = ProfileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            # If the user already has a profile, update it; otherwise, create a new one
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('profile')  # Redirect to the profile page or update the URL name accordingly

    context = {'form': form}
    return render(request, 'NiceAdmin/users-profile.html', context)


def dashBoard(request):
    """
    View for rendering the dashboard.
    """
    # Get PDFs for the logged-in user
    user_pdfs = Course.objects.all()

    # Get Seminars for the logged-in user
    user_seminars = Seminar.objects.all()
    notification = Notification.objects.all()
    best = BestStudent.objects.all()

    context = {'user_pdfs': user_pdfs, 'user_seminars': user_seminars, 'notification': notification, 'best': best}
    return render(request, 'NiceAdmin/index.html', context)


def contactPage(request):
    """
    View for rendering the contact page.
    """
    context = {}
    return render(request, 'department/contact.html', context)


def aboutPage(request):
    """
    View for rendering the about page.
    """
    context = {}
    return render(request, 'department/about.html', context)


def lecturers(request):

    lect = Lecturer.objects.all()

    context = {'lect': lect}
    return render(request, 'NiceAdmin/lecturer.html', context)

def nonacedemic(request):

    lect = AdministrativeStaff.objects.all()

    context = {'lect': lect}
    return render(request, 'NiceAdmin/nonacedemy.html', context)

def Technicalpage(request):

    lect = Technical.objects.all()

    context = {'lect': lect}
    return render(request, 'NiceAdmin/technical.html', context)