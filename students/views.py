# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
    students = ({'id': 1,
                 'first_name': u'Mexicano',
                 'last_name': u'Man',
                 'ticket': 1488,
                 'image': 'img/hobo.jpg'},

                {'id': 2,
                 'first_name': u'Johnny',
                 'last_name': u'Catsville',
                 'ticket': 1349,
                 'image': 'img/cat.jpg'},

                {'id': 3,
                 'first_name': u'Bad',
                 'last_name': u'Santa',
                 'ticket': 666,
                 'image': 'img/santa.jpg'},)
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
