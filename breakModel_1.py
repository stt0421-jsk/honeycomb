# Python code to break the Honeycomb Security Model 1
import math
import sys
import mpmath as mp
from decimal import *



def log(data, newData=""):
    print("LOG: ", data + str(newData))

def default(n1, n2, n3, dp_k, data):
    print("INTRUDER KNOWS EVERY DATA EXCEPT FOR THE LOCATION OF 'K'")
    print("\n")
    print("CALCULATING...")
    print("\nCALCULATION LOG")
    print("\n")
    # log("MPMATH SETTINGS")
    # mp.prec = 500
    # mp.dps = 100
    # print(mp)
    getcontext().prec = 2000
    data_default = (((dp_k+n2)//(n2*n1))**(Decimal(1)/Decimal(r3)))
    log("VALUE OF RENDERED 'DATA' = ", data_default)
    log("FETCHING THE MINIMUM POSSIBLE VALUE OF r2")
    min_r2_data = min(n1, n2, n3)
    log("SUCCESS, MIN VALUE = ", min_r2_data)
    
    log("EXPERIMENTING WITH MINIMUM VALUE ", min_r2_data)
    min_r2 = 1
    n_list = [n1, n2, n3]
    n_list.remove(min_r2_data)

    log("r1 = ", n_list[1])
    log("r3 = ", n_list[0])
    print("\n")
    while (min_r2 < min_r2_data):
        dp_m = int(dp_k)
        #log("dp_m = ", dp_m)
        log("r2 = ", min_r2)
        getcontext().prec = 2000
        data_m = (((dp_m+(min_r2*(min_r2_data**min_r2_data)))//(min_r2_data*n_list[1]))**(Decimal(1)/Decimal(n_list[0])))
        if (math.isclose(data_m, data, abs_tol=Decimal(0.000000000000000000000000000000000001))) == True:
            print("\n")
            print("*****************************************************")
            print("*****************************************************")
            print("******************** MATCH FOUND ********************")
            print("*****************************************************")
            print("*****************************************************")
            print("ORIGINAL DATA: ", data)
            print("RENDERED DATA: ", data_m)
            print("r1 = ", n_list[1])
            print("r2 = ", min_r2_data)
            print("r3 = ", n_list[0])
            print("INTRUDER LOCATION = ", min_r2)
            min_r2 += 1
            #break
        else:
            log("VALUE OF data_m = ", data_m)
            print("\n")
            log("** NO MATCH, MOVING ON")
            print("\n")
            min_r2 += 1
    print("\n\n")

    log("CHANGE r1, r3 VALUES")
    min_r2 = 1
    log("r1 = ", n_list[0])
    log("r3 = ", n_list[1])
    print("\n")
    while (min_r2 < min_r2_data):
        dp_m = int(dp_k)
        #log("dp_m = ", dp_m)
        log("r2 = ", min_r2)
        log("min_r2_data = ", min_r2_data)
        log("n_list[1] = ", n_list[1])
        log("n_list[0] = ", n_list[0])
        getcontext().prec = 2000
        data_m = (((dp_m+(min_r2*(min_r2_data**min_r2_data)))//(min_r2_data*n_list[0]))**(Decimal(1)/Decimal(n_list[1])))
        if (math.isclose(data_m, data, abs_tol=Decimal(0.000000000000000000000000000000000001))) == True:
            print("\n")
            print("*****************************************************")
            print("*****************************************************")
            print("******************** MATCH FOUND ********************")
            print("*****************************************************")
            print("*****************************************************")
            print("\n")
            print("** ORIGINAL DATA: ", data)
            print("** RENDERED DATA: ", data_m)
            print("** r1 = ", n_list[0])
            print("** r2 = ", min_r2_data)
            print("** r3 = ", n_list[1])
            print("** INTRUDER LOCATION = ", min_r2)
            min_r2 += 1
            print("\n\n")
            #break
        else:
            log("VALUE OF data_m = ", data_m)
            log("NO MATCH, MOVING ON")
            print("\n\n")
            min_r2 += 1
    print("\n\n")    


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
dp = int(r1*r2*(data**r3))
print("CALCULATED VALUE OF 'DATA PRIME' = ", dp)
print("\n\n")
k = int(input("LENGTH FROM DATA ORIGIN TO 'K' = "))
print("\n")
dp_k = dp - k*(r2**r2)
print("INTRUDER GETS 'DATA PRIME' VALUE AS = ", dp_k)

default(r1, r2, r3, dp_k, data)
