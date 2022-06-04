
from django.forms.forms import Form
from django.http import request
from django.shortcuts import render
from fst_app import forms
import fst_app
from fst_app .models import stu_form

def index(request):
    stu_list=stu_form.objects.order_by('fname')
    diction={'title':'index','start':stu_list}
    return render (request,'fst_app/index.html',context=diction)

def student(request):
    form=forms.stu_reg()
    if request.method =="POST":
        form=forms.stu_reg(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)


    diction={'title':'student form','start':form}
    return render (request,'fst_app/sform.html',context=diction)

def stuinfo(request,student_id):
    stuinfo=stu_form.objects.get(pk=student_id)
    diction={'start':stuinfo}
    return render(request,'fst_app/stu_info.html',context=diction)

def stuup(request,student_id):
    stuinfo=stu_form.objects.get(pk=student_id)
    form=forms.stu_reg(instance=stuinfo)

    if request.method== 'POST':
        form=forms.stu_reg(request.POST,instance=stuinfo)
    if form.is_valid():
            form.save(commit=True)
            return index(request)
    dection={"start":form}
    return render(request,'fst_App/stu_update.html',context=dection)

def studlt(request,student_id):
    student=stu_form.objects.get(pk=student_id).delete()
    diction={'dlt_mgs':'DELETE DONE'}
    return render(request,'fst_app/stu_delete.html',context=diction)