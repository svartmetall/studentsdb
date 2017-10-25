# -*- coding: utf-8 -*-

from django.shortcuts import render
import calendar


def journal_list(request):
    journal = ({'id': 1,
                'student_name': u'Joseph Kobzon'},

               {'id': 2,
                'student_name': u'Nikolay Baskov'},

               {'id': 3,
                'student_name': u'Boris Moiseev'},)
    return render(request, 'students/journal.html', {'journal': journal, 'days': _days_list()})


def _days_list(year=2014, month=10):
    week_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
    month_range = calendar.monthrange(year, month)
    current_week_days = week_days[month_range[0]:] + week_days[:month_range[0]]
    days_range = [i for i in range(1, month_range[1] + 1)]
    month_calendar = []
    for i in range(len(days_range)):
        day = current_week_days[i % 7] + ' ' + str(days_range[i])
        month_calendar.append(day)

    return month_calendar
