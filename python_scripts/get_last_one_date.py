# -*- coding:utf-8 -*-
# (c) 2017, Ji Dongdong <jidongdong@cnnic.cn> 
#  
# 模块用于计算最近1天，最近1周，最近1个月，最近1年的时间

import datetime


def day(today):
    dayscount = datetime.timedelta(days=1)
    date_from = (today - dayscount).strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def week(today):
    dayscount = datetime.timedelta(weeks=1)
    date_from = (today - dayscount).strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def month(today):
    dayscount = datetime.timedelta(days=(today.day - 1))
    date_from = datetime.datetime(today.year, today.month-1, 1, today.hour, today.minute, today.second) + dayscount
    date_from = date_from.strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])


def year(today):
    date_from = datetime.datetime(today.year-1, today.month, today.day, today.hour, today.minute, today.second)
    date_from = date_from.strftime('%Y-%m-%d %H:%M:%S')
    date_to = today.strftime('%Y-%m-%d %H:%M:%S')
    print '--'.join([str(date_from), str(date_to)])

if __name__ == '__main__':
    today_datetime = datetime.datetime.now()
    day(today_datetime)
    week(today_datetime)
    month(today_datetime)
    year(today_datetime)