# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = ({'id': 1,
               'group_name': u'SLP-666',
               'boss_name': u'Tom Arraya'},

              {'id': 2,
               'group_name': u'MLTH-88',
               'boss_name': u'Olexiy Thuleseeker'},

              {'id': 3,
               'group_name': u'ART-15',
               'boss_name': u'Mat Best'})
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
