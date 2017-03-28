#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.
import datetime


def calculate_day_interval(date_time):
    """
    calculate days interval from date to today
    :param {datetime.datetime} date_time: datetime
    :return {int} days
    """
    if isinstance(date_time, datetime.datetime):
        days = (datetime.date.today() - date_time.date()).days
        if days >= 0:
            return days
    return '--'


def get_previous_month_day_from_today():
    """
    get date of previous month form today
    :return:{datetime.date}
    """
    today = datetime.date.today()
    if today.month - 1 == 0:
        previous_month_date = datetime.date(today.year - 1, 12, today.day)
    else:
        previous_month_date = datetime.date(today.year, today.month - 1, today.day)

    return previous_month_date
