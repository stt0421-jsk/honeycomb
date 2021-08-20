# Python code to break the Honeycomb Security Model 1
import math
import sys

def log(data, newData=""):
    print("LOG: ", data + str(newData))

def default(n1, n2, n3, dp_k, data):
    print("INTRUDER KNOWS EVERY DATA EXCEPT FOR THE LOCATION OF 'K'")
    print("\n")
    print("CALCULATING...")
    print("\nCALCULATION LOG")
    print("\n")
    # data_default = (((dp_m+min_r2)/(min_r2_data*n_list[1]))**(1.0/float(n_list[0])))
    log("VALUE OF RENDERED 'DATA' = ", )
    log("FETCHING THE MINIMUM POSSIBLE VALUE OF r2")
    min_r2_data = min(n1, n2, n3)
    log("SUCCESS, MIN VALUE = ", min_r2_data)
    
    log("EXPERIMENTING WITH MINIMUM VALUE ", min_r2_data)
    min_r2 = 0
    n_list = [n1, n2, n3]
    n_list.remove(min_r2_data)

    log("r1 = ", n_list[1])
    log("r3 = ", n_list[0])
    print("\n")
    while (min_r2 < min_r2_data):
        dp_m = dp_k
        log("r2 = ", min_r2)
        data_m = (((dp_m+min_r2)/(min_r2_data*n_list[1]))**(1.0/float(n_list[0])))
        log("TRUE/FALSE - ", math.isclose(data_m, data))
        if (math.isclose(data_m, data)) == True:
            print("*********************************")
            print("********** MATCH FOUND **********")
            print("*********************************")
            print("ORIGINAL DATA: ", data)
            print("RENDERED DATA: ", data_m)
            print("r1 = ", n_list[1])
            print("r2 = ", min_r2_data)
            print("r3 = ", n_list[0])
            print("INTRUDER LOCATION = ", min_r2)
            break
        else:
            log("VALUE OF data_m = ", data_m)
            log("NO MATCH, MOVING ON")
            print("\n")
            min_r2 += 1
    print("\n\n")

    log("CHANGE r1, r3 VALUES")
    min_r2 = 0
    log("r1 = ", n_list[0])
    log("r3 = ", n_list[1])
    print("\n")
    while (min_r2 < min_r2_data):
        dp_m = dp_k
        log("r2 = ", min_r2)
        data_m = (((dp_m+min_r2)/(min_r2_data*n_list[0]))**(1.0/float(n_list[1])))
        log("TRUE/FALSE - ", math.isclose(data_m, data))
        if (math.isclose(data_m, data)) == True:
            print("\n\n\n")
            print("*****************************************************")
            print("******************** MATCH FOUND ********************")
            print("*****************************************************")
            print("ORIGINAL DATA: ", data)
            print("RENDERED DATA: ", data_m)
            print("r1 = ", n_list[0])
            print("r2 = ", min_r2_data)
            print("r3 = ", n_list[1])
            print("INTRUDER LOCATION = ", min_r2)
            break
        else:
            log("VALUE OF data_m = ", data_m)
            log("NO MATCH, MOVING ON")
            print("\n")
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

data = float(input("VALUE OF 'DATA' = "))
print("\n")
r1 = float(input("LENGTH OF ROUTE 1 = "))
r2 = float(input("LENGTH OF ROUTE 2 = "))
r3 = float(input("LENGTH OF ROUTE 3 = "))
print("\n")
print("CALCULATING 'DATA PRIME'...")
dp = float(r1*r2*(data**r3))
print("CALCULATED VALUE OF 'DATA PRIME' = ", dp)
print("\n\n")
k = float(input("LENGTH FROM DATA ORIGIN TO 'K' = "))
print("\n")
dp_k = dp - k
print("INTRUDER GETS 'DATA PRIME' VALUE AS = ", dp_k)

default(r1, r2, r3, dp_k, data)
