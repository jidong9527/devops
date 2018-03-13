# -*- coding:utf-8 -*-
# (c) 2017, Ji Dongdong <jidongdong@cnnic.cn> 
#  
# 模块用于计算最近N天，最近N周，最近N个月，最近N年的时间

import datetime


def day(today, num):
    dayscount = datetime.timedelta(days=num)
    date_from = (today - dayscount).strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def week(today, num):
    dayscount = datetime.timedelta(weeks=num)
    date_from = (today - dayscount).strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def month(today, num):
    month = today.month - num
    if month > 0:
        date_from = datetime.datetime(today.year, month, today.day, today.hour,
                                      today.minute, today.second)
    else:
        date_from = datetime.datetime(today.year-1, 12+month, today.day,
                                      today.hour, today.minute, today.second)
    date_from = date_from.strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def year(today, num):
    if num >= 1000:
        return
    date_from = datetime.datetime(today.year-num, today.month, today.day,
                                  today.hour, today.minute, today.second)
    date_from = date_from.strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])

if __name__ == '__main__':
    today_datetime = datetime.datetime.now()
    number = 4
    day(today_datetime, number)
    week(today_datetime, number)
    month(today_datetime, number)
    year(today_datetime, number)
