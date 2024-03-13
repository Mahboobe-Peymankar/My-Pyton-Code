name = input ( "Please Enter your name...")
family = input ( "Please enter your surname... ")
a = float (input ( "Please enter your first score...") )
b = float (input ( "Please enter your second score...") )
c = float (input ("Please enter your third score...") )

if (a > 0 and b > 0 and c > 0 and a <= 20 and b <= 20 and c <= 20) :
    avg = (a+b+c)/3
    print ("The average of", name, " ", family ,"is..." , avg )
    if (avg < 12):
        print ("This student is failed ")
    elif (avg < 17):
        print ("This student is normal ")
    else:
        print ("This student is great ")
else :
    print ("Please enter the correct number between 0 and 20")

