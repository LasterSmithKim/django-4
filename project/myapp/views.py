from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")
def detail(request,num):
    return HttpResponse("detail - %s"%num)

from .models import Grades,Students
def grades(request):
    #去模型里取数据
    gradeList = Grades.objects.all()
    #将数据传递给模板，渲染成页面,返回给用户
    return render(request,'myapp/grades.html',{'grades':gradeList})

def students(request):
    #去模型里取数据
    studentsList = Students.objects.all()
    #将数据传递给模板，渲染成页面,返回给用户
    return render(request,'myapp/students.html',{'students':studentsList})

def gradesstudents(request,num):
    #获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    #获得班级下的所有学生信息列表
    studentsList = grade.students_set.all()
    return render(request, 'myapp/students.html', {'students': studentsList})