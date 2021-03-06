from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import ActivityForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404


from .models import *



# Create your views here.
@login_required(login_url="/login")
def activity(response):
    activity = Activity.objects.all()
    return render(response, 'activity/activity.html', {'activity':activity})


@login_required(login_url="/login")
def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activity')
    else:
        form = ActivityForm()
        title ="none"
    return render(request, 'activity/activity_edit.html', {'form': form, 'title':title})


@login_required(login_url="/login")
def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('activity')
    else:
        form = ActivityForm(instance=activity)
        title ="none"

    return render(request, 'activity/activity_edit.html', {'form': form, 'title':title})

@login_required(login_url="/login")
def activity_enroll(request,pk):
    activity = get_object_or_404(Activity, pk=pk)

    activity.enrolled_users.add(request.user)
    
    return redirect('activity')
