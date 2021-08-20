"""
cf) x의 n제곱근: x**(1.0/n)
D = ((DP + r2)/(r1*r2))**(1.0/r3)
"""

# Python code to break the Honeycomb Security Model 1

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
dp_k = dp - k + 1
print("INTRUDER GETS 'DATA PRIME' VALUE AS = ", dp_k)

default(r1, r2, r3, data)

def log(data):
    print("LOG: ", data)

def default(n1, n2, n3, data):
    print("INTRUDER KNOWS EVERY DATA EXCEPT FOR THE LOCATION OF 'K'")
    print("\n")
    print("CALCULATING...")
    print("\nCALCULATION LOG")
    
    log("FETCHING THE MINIMUM POSSIBLE VALUE OF r2")
    min_r2_data = min(n1, n2, n3)
    log("SUCCESS, MIN VALUE = ", min_r2_data)
    
    log("EXPERIMENTING WITH MINIMUM VALUE ", min_r2_data)
    min_r2 = 0
    n_list = [n1, n2, n3]
    n_list.remove(min_r2_data)

    while (min_r2 < min_r2_data):
        dp_m = dp_k + min_r2
        log("r2 = ", min_r2_data)
        log("r1 = ", n_list[1])
        log("r3 = ", n_list[0])
        data_m = (((dp_m + min_r2_data)/min_r2_data*n_list[1])**(1.0/float(n_list[0])))
        if data_m = data:
            log("***** MATCH FOUND *****")
            log("data_m FOUND = ", data_m)
            break
        else:
            log("NO MATCH, MOVING ON")
            print("\n")
            min_r2 += 1



"""
def calc(case):
    if case = 1:
        print("INTRUDER KNOWS VALUE OF r1, r2, r3")
        print("BUT DOES NOT KNOW WHICH IS WHICH")
        print("\n")
"""