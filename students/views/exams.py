# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from ..models.exams import Exam


def exams_list(request):
    exams = Exam.objects.all()

    # Try to order groups list.
    order_by = request.GET.get('order_by', 'title')
    if order_by in ('title', 'date', 'teacher', 'exam_group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '0') == '1':
            exams = exams.reverse()

    # Paginator.
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams_list.html', {'exams': exams})


def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')


def exams_edit(request, gid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % gid)


def exams_delete(request, gid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % gid)
