# -*- coding:utf-8 -*-
# (c) 2017, Ji Dongdong <jidongdong@cnnic.cn> 
#  
# 模块用于计算上N天，上N周，上N个月，上N年的起止时间

import datetime


def day(today, num):
    dayscount = datetime.timedelta(days=num)
    dayfrom = today - dayscount
    dayto = today - datetime.timedelta(days=1)
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return {
        "start": date_from.strftime('%Y-%m-%d %H:%M:%S'),
        "end": date_to.strftime('%Y-%m-%d %H:%M:%S')
    }


def week(today, num):
    dayscount = datetime.timedelta(days=today.isoweekday())
    dayto = today - dayscount
    nweek_days = datetime.timedelta(days=13)
    dayfrom = dayto - nweek_days
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0,
                                  0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return {
        "start": date_from.strftime('%Y-%m-%d %H:%M:%S'),
        "end": date_to.strftime('%Y-%m-%d %H:%M:%S')
    }


def month(today, num):
    dayscount = datetime.timedelta(days=today.day)
    dayto = today - dayscount
    nmonth_days = datetime.timedelta(weeks=4*num)
    dayfrom = today - nmonth_days
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, 1, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    return {
        "start": date_from.strftime('%Y-%m-%d %H:%M:%S'),
        "end": date_to.strftime('%Y-%m-%d %H:%M:%S')
    }


def year(today, num):
    date_from = datetime.datetime(today.year-num, 1, 1, 0, 0, 0)
    date_to = datetime.datetime(today.year-1, 12, 31, 23, 59, 59)
    return {
        "start": date_from.strftime('%Y-%m-%d %H:%M:%S'),
        "end": date_to.strftime('%Y-%m-%d %H:%M:%S')
    }

if __name__ == '__main__':
    today_datetime = datetime.datetime.now()
    number = 2
    day(today_datetime, number)
    week(today_datetime, number)
    month(today_datetime, number)
    year(today_datetime, number)
