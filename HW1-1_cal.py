import math
print ("welcome to my calculator")
print (" + : Sum " )
print ( "- : sub " )
print ( "* : mul " )
print ( "/ : div " )
print ( "--------" )
print ( "sin : sin " )
print ( "cos : cos " )
print ( "tan : tan " )
print ( "cot : cot " )
print ( "--------" )
print ( "sqr : square")
print ( "sqrt : square root")
print ( "! : factorial" )
print ( "--------" )
op = input ( "please enter your choice:... " )

if( op ==  "+" or op == "-" or op == "*" or op == "/"):
    A = float (input("Enter the first number..."))
    B = float (input("Enter the second number..."))
    if( op == "+"):
        result = A + B
    elif (op == "-"):
        result = A - B
    elif (op == "*"):
        result = A * B
    else :
        result = A / B
elif ( op == "sin" or op == "cos" or op == "tan" or op == "cot" ):
    print ("dg : degree")
    print ("ra : radian")
    C = input ("Please enter the angle unit ...")
    A = float (input( "Enter your angel..." ))
    if ( C == "dg" ):
        A = A * math.pi/180
    if ( op == "sin"):
        result = math.sin(A)
    elif( op == "cos"):
        result = math.cos (A)
    elif( op == "tan"):
        result = math.tan (A)
    elif( op == "cot"):
        result = math.cot (A)
elif (op == "sqr" or op == "sqrt"):
    A = float (input ("Enter a number..."))
    if( op == "sqr"):
        B = float (input ( " Enter a power number..."))
        result = A ** B  
    else:
        if( A < 0):
            print ("Error : You should enter a positive number ")
        result = A ** 0.5
elif (op == "!"):
    A = int (input ("Enter an intiger number..."))
    if( A < 0):
        print ("Error : You should enter a positive number ")
    else:
        result = math.factorial ( A )

print (result)

            
