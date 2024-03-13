weight = float (input ( "please enter your weight in kg ..." ) )
height = float (input ( "please enter your height in m ..." ) )
BMI = weight/( height**2 )
if ( BMI < 18.5 ):
    print ( "Underweight" )
elif ( BMI < 24.9 ):
    print ( "Normal weight" )
elif ( BMI < 29.9 ):
    print ( "oOverweight" )
elif ( BMI < 34.9 ):
    print ( "Obesity" )
else:
    print ( "Extreme Obesity" )