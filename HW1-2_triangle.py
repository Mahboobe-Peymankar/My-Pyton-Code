A = float (input ("enter the first positive number..."))
B = float (input ("enter the second positive number..."))
C = float (input ("ente3r the third positive number..."))

if (A > 0 and B > 0 and C > 0 ):
    if(A + B > C and A + C > B and B + C > A):
        print("It is possible to create a triangle with these numbers")
    else:
        print("Error: Creating a triangle is impossible by these numbers")
else:
    print("Error: Enter the positive numbers")