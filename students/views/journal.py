# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import calendar


from ..models.students import Student


def journal_list(request):
    journal = Student.objects.all()

    # Try to order students list.
    order_by = request.GET.get('order_by', 'last_name')
    if order_by == 'last_name':
        journal = journal.order_by(order_by)
        if request.GET.get('reverse', '0') == '1':
            journal = journal.reverse()

    # Paginator.
    paginator = Paginator(journal, 3)
    page = request.GET.get('page')
    try:
        journal = paginator.page(page)
    except PageNotAnInteger:
        journal = paginator.page(1)
    except EmptyPage:
        journal = paginator.page(paginator.num_pages)

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
