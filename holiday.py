#!/usr/bin/env python3
"""
the target to spend as much as time as possible in your dreamed vacation, 
the problem is that there is only one plane per week to your destination,
the plane departs every Monday and arrives every Sunday.
there is no other way to get to the destination, 
it means you can spend only whole week there, 
you are give which month your vacation starts and in which month it ends
your vacation period starts on the first day of the beginning month and ends on the last day of the ending month,
the year is known as well

for example if your vacation lasts from July to September in 2008, then it starts on 1st July 2008 and ends 30th September 2008, 

your task is to calculate how many weeks you will spend in your dreamed vacation, given:
   -- the month when the vacation begins
   -- the month when the vacation ends
   -- the year when the vacation takes place
   -- the day of the week for 1st January in the vacation year, 

"""

def solution(Y,A,B,W):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap = (Y % 4 == 0)
    if leap: month_days[1] += 1

    start_month = months.index(A)
    end_month = months.index(B)

    firstDay = days.index(W) + sum(month_days[0:start_month])
    daysInAB = sum(month_days[start_month:end_month+1])

    numberOfWeeks = int(daysInAB/7) if (firstDay%7==0) else int((daysInAB - (7-firstDay%7))/7)
    # print(firstDay)
    #print(days[firstDay%7])
    #print(month_days[start_month:end_month+1])
    #print(daysInAB)

    return numberOfWeeks


print(solution(2014,'April','May','Wednesday'))