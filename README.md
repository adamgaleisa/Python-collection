# Python-collection

Plane reservation

you are processin plane seat reservations, The plan has N rows of seats, numbered from 1 to N
there are ten seats in each raw labelled from A to K with letter I omitted) as shown below


##      A&nbsp;B&nbsp;C&nbsp;&nbsp;&nbsp;&nbsp;D E F G&nbsp;&nbsp;&nbsp;&nbsp;H&nbsp;J&nbsp;K  
##   1  |&nbsp;|&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;| &nbsp;|&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;|&nbsp;|  
##   2  |&nbsp;|&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;| &nbsp;|&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;|&nbsp;| 
   
Some of the seats are already reserved, the list of reserved seats is given as string S(of length M) containing seat numbers 
separated by single spaces : for example "1A 3C 2B 40G 5A", the reserved seats can be listed in S in any order.

your task is to allocate seats for as many three person families as possible, a three person family occupies three seats that are next to each other in the same raw.
Seats across aisle (such as 2C and 2D) are not considered to be next to each other, obviously, each avaialbe seat can't be taken by more then one family.

for instance N = 2, S ="1A 2F 1C", your function should return 4, 

