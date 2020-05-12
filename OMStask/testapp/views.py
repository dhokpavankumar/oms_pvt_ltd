from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.models import student
from testapp.forms import studentForm,SignupForm,User
from django.http import HttpResponseRedirect


def home_page_view(request):
    return render(request, 'testapp/home.html')

@login_required
def student_view(request):
    form=studentForm()
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request, 'testapp/addstudent.html', {'form':form})

@login_required
def list_information_view(request):
    student_list=student.objects.all()
    return render(request, 'testapp/listinformation.html', {'student_list':student_list})

def logout_view(request):
    return render(request, 'testapp/logout.html')

def Signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html',{'form':form})



from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render

class Pdf(View):

    def get(self, request):
        data = student.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'data': data,
            'request': request
        }
        return Render.render('pdf.html', params)




