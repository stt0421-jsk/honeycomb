# Honeycomb Security Simulator
# Written in Python, by Joonsung Kim

import random
from decimal import *

r1 = int(input("LENGTH OF Route 1: "))
r2 = int(input("LENGTH OF Route 2: "))
r3 = int(input("LENGTH OF Route 3: "))
print("\n")
data = int(input("DATA: "))

print("\n\nA HAS SENT INITIALIZER TO B")
print("B HAS RECIEVED INITIALIZER")

ar12 = random.randrange(1, 1001)
ar23 = random.randrange(1, 1001)
ar31 = random.randrange(1, 1001)
list_ar = [ar12, ar23, ar31]

def recv_1(original, howfar):
    return original - howfar

print("\nRANDOM NUMBERS FOR A-PING WERE CHOSEN")
print(list_ar)

print("\nPINGING NUMBERS IN ROUTE")
k12 = recv_1(recv_1(ar12, r2), r1)
k23 = recv_1(recv_1(ar23, r3), r2)
k31 = recv_1(recv_1(ar31, r1), r3)
print("RECIEVED PINGED NUMBERS")
list_k = [k12, k23, k31]
print(list_k)

a = ar12 - k12
b = ar23 - k23
c = ar31 - k31
print("\nr1 + r2 = ", a)
print("r2 + r3 = ", b)
print("r3 + r1 = ", c)

r1n = (a - b + c)/2
r2n = (a + b - c)/2
r3n = (- a + b + c)/2
print("\nLINEAR ALGEBRAIC EXPRESSIONS SOLVED")
print("r1 = ", r1n)
print("r2 = ", r2n)
print("r3 = ", r3n)
if r1n==r1 and r2n==r2 and r3n==r3:
    print("\nADMIN INPUT AND CALCULATION VALUE IS SAME")
else:
    print("\nVALUE NOT SAME, ABORT")

list_bpr = [r1, r2, r3]
print("\nRoute LENGTHS WERE MANUALY CHOSEN FOR B-PING")
print(list_bpr)

print("\nPINGING NUMBERS IN ROUTE")
arec1 = recv_1(r1, r1)
arec2 = recv_1(r2, r2)
arec3 = recv_1(r3, r3)
print("A RECIEVED THE PINGED NUMBERS")

print("COMPARING RECIEVED NUMBERS TO 0")

if arec1==0 and arec2==0 and arec3==0:
    print("\nRECIEVED VALUES ARE 0, MOVING ON")
else:
    print("\nVALUE NOT 0, ABORT")

br12 = random.randrange(1, 1001)
br23 = random.randrange(1, 1001)
br31 = random.randrange(1, 1001)
list_br = [br12, br23, br31]

print("\nRANDOM NUMBERS FOR B DATA FETCH WERE CHOSEN")
print(list_br)

print("\nDIVIDING DATA INTO RANDOM PIECES")
if data%2==0:
    d1 = random.randrange(1, data/2 + 1)
    d2 = random.randrange(1, data/2 + 1)
    d3 = data - (d1 + d2)
else:
    d1 = random.randrange(1, (data+1)/2 + 1)
    d2 = random.randrange(1, (data+1)/2 + 1)
    d3 = data - (d1 + d2)
print("SUCCEEDED")
print("VALUE OF D1, D2, D3")
list_d = [d1, d2, d3]
print(list_d)

print("\nPINGING FIRST DATA")
ab12 = recv_1(br12, r1)
ab12 += d1
ab12 = recv_1(ab12, r2)
print("B RECIEVED: ", ab12)

print("\nPINGING SECOND DATA")
ab23 = recv_1(br23, r2)
ab23 += d2
ab23 = recv_1(ab23, r3)
print("B RECIEVED: ", ab23)

print("\nPINGING THIRD DATA")
ab31 = recv_1(br31, r3)
ab31 += d3
ab31 = recv_1(ab31, r1)
print("B RECIEVED: ", ab31)

print("\nCALCULATING FULL DATA")
full_val = (ab12 + ab23 + ab31) - (br12 + br23 + br31) + 2*(r1 + r2 + r3)
print("\n\nORIGINAL DATA FROM A IS: ", full_val)
print("\n\n\nTASK COMPLETED")

exit()