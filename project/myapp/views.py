from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    #return HttpResponse("hello world")
    return render(request,'myapp/index.html')
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
    studentsList = Students.stuObj1.all()
    #将数据传递给模板，渲染成页面,返回给用户
    return render(request,'myapp/students.html',{'students':studentsList})

#显示前5条学生
def students3(request):
    studentsList = Students.stuObj1.all()[0:5]
    return render(request, 'myapp/students.html', {'students': studentsList})

#分页显示学生
def stupage(request,page):
    #0-5 5-10 10-15
    # 1   2     3
    page = int(page)
    studentsList = Students.stuObj1.all()[(page-1)*5:page*5]
    return render(request, 'myapp/students.html', {'students': studentsList})

#
def studentssearch(request):
    #studentsList = Students.stuObj1.all().filter(sname__contains="张")
    #studentsList = Students.stuObj1.all().filter(sname__startswith="张")
    #studentsList = Students.stuObj1.all().filter(sname__endswith="1")
    #studentsList = Students.stuObj1.all().filter(id__in=[1,2,4,5,10])
    #studentsList = Students.stuObj1.all().filter(sage__gt=30)
    studentsList = Students.stuObj1.all().filter(lastTime__year=2017)


    return render(request,'myapp/students.html',{'students':studentsList})


def gradesstudents(request,num):
    #获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    #获得班级下的所有学生信息列表
    studentsList = grade.students_set.all()
    return render(request, 'myapp/students.html', {'students': studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华",34,True,"我叫刘德华",grade,)
    stu.save()
    return HttpResponse("保存")

def addstudent1(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj1.createStudent("张学友1",22,True,"我就张学友",grade)
    stu.save()
    return HttpResponse("保存")

