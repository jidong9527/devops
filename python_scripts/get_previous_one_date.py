# -*- coding:utf-8 -*-
# (c) 2017, Ji Dongdong <jidongdong@cnnic.cn> 
#  
# 模块用于计算上1天，上1个月，上1年的时间

import datetime


def day(today):
    oneday = datetime.timedelta(days=1)
    day = today - oneday
    date_from = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
    date_to = datetime.datetime(day.year, day.month, day.day, 23, 59, 59)
    print '--'.join([str(date_from), str(date_to)])


def week(today):
    dayscount = datetime.timedelta(days=today.isoweekday())
    dayto = today - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0,
                                  0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    print '--'.join([str(date_from), str(date_to)])


def month(today):
    dayscount = datetime.timedelta(days=today.day)
    dayto = today - dayscount
    date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    print '--'.join([str(date_from), str(date_to)])


def year(today):
    date_from = datetime.datetime(today.year-1, 1, 1, 0, 0, 0)
    date_to = datetime.datetime(today.year-1, 12, 31, 23, 59, 59)
    print '--'.join([str(date_from), str(date_to)])

if __name__ == '__main__':
    today_datetime = datetime.datetime.now()
    day(today_datetime)
    week(today_datetime)
    month(today_datetime)
    year(today_datetime)