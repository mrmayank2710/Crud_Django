from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        
        fm = StudentRegistration(request.POST or None)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            regst = User(name=nm, email=em, password = ps)
            regst.save()
            fm = StudentRegistration()
            return redirect(add_show)
           
             
    else:
  
        fm = StudentRegistration()
    stud = User.objects.all()    
        
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu': stud})



def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect(add_show)
    

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
                  
    return render(request, 'enroll/updatestudent.html', {'form':fm})
    