# Python-collection

## 1) Plane reservation

you are processing plane seat reservations, The plan has N rows of seats, numbered from 1 to N
there are ten seats in each raw labelled from A to K with letter I omitted) as shown below


##      A&nbsp;B&nbsp;C&nbsp;&nbsp;&nbsp;&nbsp;D E F G&nbsp;&nbsp;&nbsp;&nbsp;H&nbsp;J&nbsp;K  
##   1  |&nbsp;|&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;| &nbsp;|&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;|&nbsp;|  
##   2  |&nbsp;|&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;| &nbsp;|&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;|&nbsp;| 
   
Some of the seats are already reserved, the list of reserved seats is given as string S(of length M) containing seat numbers 
separated by single spaces : for example "1A 3C 2B 40G 5A", the reserved seats can be listed in S in any order.

your task is to allocate seats for as many three person families as possible, a three person family occupies three seats that are next to each other in the same raw.
Seats across aisle (such as 2C and 2D) are not considered to be next to each other, obviously, each available seat can't be taken by more then one family.

for instance N = 2, S ="1A 2F 1C", your function should return 4, 


## 2) Maximizing holiday

The target to spend as much as time as possible in your dreamed vacation, 
The problem is that there is only one plane per week to your destination,
The plane departs every Monday and arrives every Sunday.
There is no other way to get to the destination, 
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

if the function is given:
Y = 2014, A="April", B="May", and W= "Wedensday", the function should return 7

## 3) Hash Iterator

two inputs, **a salt** and **an integer X**, and generates a 
**10-character string** over the course of a large number of iterations.
how to run 

#### echo "machine-learning,4" >/tmp/input_file.txt
#### ./hash_iterator.py </tmp/input_file.txt


