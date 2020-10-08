#!/usr/bin/env python3
"""
you are processin plane seat reservations, The plan has N rows of seats, numbered from 1 to N
there are ten seats in each raw labelled from A to K with letter I omitted) as shown below


      A B C    D E F G    H J K
   1  | | |    | | | |    | | |
   2  | | |    | | | |    | | |
   
Some of the seats are already reserved, the list of reserved seats is given as string S(of length M) containing seat numbers 
separated by single spaces : for example "1A 3C 2B 40G 5A", the reserved seats can be listed in S in any order.

your task is to allocate seats for as many three person families as possible, a three person family occupies three seats that are next to each other in the same raw.
Seats across aisle (such as 2C and 2D) are not considered to be next to each other, obviously, each avaialbe seat can't be taken by more then one family.

for instance N = 2, S ="1A 2F 1C", your function should return 4, 
"""

def solution(N,S):
    taken = S.split()
    seats = [["A","B","C"],["D","E","F","G"],["H","J","K"]]
    total_available = 0
    for i in range(1,N+1):
        available = [[1 if f"{i}{x}" in taken else 0 for x in group] for group in seats]
        if not (1 in available[0]): total_available += 1
        if not (1 in available[2]): total_available += 1
        if ((available[1][0] == 0 or available[1][3] ==0) and available[1][1] == 0 and available[1][2] == 0): total_available += 1

    return total_available 


print(solution(2,"1A 2F 1C"))


