from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .models import *
# Create your views here.
from django.shortcuts import render

def regform(request):
    if request.method == "POST":
        id_no = request.POST.get("idno")
        img = request.FILES.get("img") 
        name = request.POST.get("name")
        age = request.POST.get("age")
        rollno = request.POST.get("rollno")
        class_name = request.POST.get("class_name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
            
        if Student.objects.filter(idno=id_no).exists() or Student.objects.filter(email=email).exists():
            messages.success(request,"This ID already exists or Email already exists")
            return render(request, "regform.html")
        else:       
            data=Student(idno=id_no,img=img,name=name,age=age,rollno=rollno,class_name=class_name,mobile=mobile,email=email,password=password)
            data.save()
            messages.success(request, "Student information added successfully.")
            return render(request, "regform.html",{'data':data})
    data=Student.objects.all()
    return render(request, "regform.html",{'data':data})


def delete(request,id):
    data=Student.objects.all()
    if request.method=="GET":
        student=Student.objects.get(pk=id)
        student.delete()
        messages.success(request, "Student information Deleted successfully.")

    return render(request, "regform.html",{'data':data})


def edit(request, id):
    student =Student.objects.get(pk=id)
    if request.method == "POST":
        id_no = request.POST.get("idno")
        img = request.FILES.get("img")
        name = request.POST.get("name")
        age = request.POST.get("age")
        rollno = request.POST.get("rollno")
        class_name = request.POST.get("class_name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if ID or email already exists excluding the current student being edited
        if Student.objects.exclude(id=id).filter(idno=id_no).exists() or Student.objects.exclude(id=id).filter(email=email).exists():
            messages.error(request, "This ID or Email already exists.")
            return render(request, "regform.html", {'data': student})

        # Update the student instance with the new data
        student.idno = id_no
        student.img = img
        student.name = name
        student.age = age
        student.rollno = rollno
        student.class_name = class_name
        student.mobile = mobile
        student.email = email
        student.password = password

        # Save the updated instance
        student.save()

        student.idno = ""
        student.img = ""
        student.name = ""
        student.age = ""
        student.rollno = ""
        student.class_name = ""
        student.mobile =""
        student.email = ""
        student.password = ""

        messages.success(request, "Student information updated successfully.")

    data = Student.objects.all()
    return render(request, "regform.html", {'data': data ,'student': student})

