
# Create your views here.
from django.utils import timezone
from django.shortcuts import render
from .models import Course, Profile

# Create your views here.

def user_profile(response):
    courses=Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    user_profile=Profile.objects.get(user=response.user)
    return render(response, "userprofile/profile.html", {'courses':courses, 'user_profile':user_profile})