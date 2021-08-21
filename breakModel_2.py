import math
from decimal import *

def log(data, newData=""):
    print("LOG: ", data + str(newData))

def model_two(n1, n2, n3, a, b, c, dp_k, data):
    print("CALCULATING...")
    print("\nCALCULATION LOG")
    print("\n")

    getcontext().prec = 2000
    data_rendered = ((dp_k + (r2 ** (2 * r2))) // (r1 * r2 * r3)) ** (Decimal(1) / Decimal(r3))
    log("VALUE OF RENDERED 'DATA' = ", data_rendered)
    print("\n")
    log("INTRUDER GETS DATA AS::")
    log("r1 = ", n1)
    log("r2 = ", n2 - c)
    log("r3 = ", n3 - a)
    log("Dp = ", dp_k + (r2 ** (2 * r2)) - (b * (r2 ** r2)))
    n1 = n1
    n2 = n2 - c
    n3 = n3 - a
    dp_int = dp_k + (r2 ** (2 * r2)) - (b * (r2 ** r2))

    a_v = 0
    b_v = 0
    c_v = 0
    print("\n")
    while a_v < n1:
        while b_v < n2 + c:
            while c_v < n3 + a:
                r1p = n1
                r2p = n2 + c_v
                r3p = n3 + a_v
                log("r1 = ", r1p)
                log("r2 = ", r2p)
                log("r3 = ", r3p)
                log("CALCULATING VALUE OF 'DATA PRIME'...")
                data_h = ((dp_int + (r2p ** (2 * r2p))) // (r1p * r2p * r3p)) ** (Decimal(1) / Decimal(r3p))
                log("RENDERING 'DATA'...")
                log("## DATA = ", data_h)
                if math.isclose(data_h, data, abs_tol = 0.002) == True:
                    print("\n")
                    print("*****************************************************")
                    print("*****************************************************")
                    print("******************** MATCH FOUND ********************")
                    print("*****************************************************")
                    print("*****************************************************")
                    print("ORIGINAL DATA: ", data)
                    print("RENDERED DATA: ", data_h)
                    print("r1 = ", r1p)
                    print("r2 = ", r2p)
                    print("r3 = ", r3p)
                    print("INTRUDER LOCATION a = ", a_v)
                    print("INTRUDER LOCATION b = ", b_v)
                    print("INTRUDER LOCATION c = ", c_v)
                    print("\n\n\n")
                else:
                    log("\n** NO MATCH, MOVING ON")
                    print("\n")
                c_v += 1
            c_v = 0
            b_v +=1
        b_v = 0
        a_v += 1

print("_______________________________________________________________________________")
print("██╗░░██╗░█████╗░███╗░░██╗███████╗██╗░░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░")
print("██║░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗████╗░████║██╔══██╗")
print("███████║██║░░██║██╔██╗██║█████╗░░░╚████╔╝░██║░░╚═╝██║░░██║██╔████╔██║██████╦╝")
print("██╔══██║██║░░██║██║╚████║██╔══╝░░░░╚██╔╝░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗")
print("██║░░██║╚█████╔╝██║░╚███║███████╗░░░██║░░░╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝")
print("╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░")
print("\n")
print("██████╗░██████╗░███████╗░█████╗░██╗░░██╗███████╗██████╗░")
print("██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("██████╦╝██████╔╝█████╗░░███████║█████═╝░█████╗░░██████╔╝")
print("██╔══██╗██╔══██╗██╔══╝░░██╔══██║██╔═██╗░██╔══╝░░██╔══██╗")
print("██████╦╝██║░░██║███████╗██║░░██║██║░╚██╗███████╗██║░░██║")
print("╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print("\n\n")
print("Ver. 0.0.1")
print("For Honeycomb Security Model 1")
print("_______________________________________________________________________________")
print("\n")
print("\n")

data = int(input("VALUE OF 'DATA' = "))
print("\n")
r1 = int(input("LENGTH OF ROUTE 1 = "))
r2 = int(input("LENGTH OF ROUTE 2 = "))
r3 = int(input("LENGTH OF ROUTE 3 = "))
print("\n")
print("CALCULATING 'DATA PRIME'...")
dp = r1*r2*r3*(data**r3)
print("CALCULATED VALUE OF 'DATA PRIME' = ", dp)
print("\n\n")
a = int(input("LENGTH OF 'INTRUDER a' = "))
b = int(input("LENGTH OF 'INTRUDER b' = "))
c = int(input("LENGTH OF 'INTRUDER c' = "))
print("\n")
dp_k = dp - (r2**(2*r2))
print("INTRUDER GETS 'DATA PRIME' VALUE AS = ", dp_k)

model_two(r1, r2, r3, a, b, c, dp_k, data)
