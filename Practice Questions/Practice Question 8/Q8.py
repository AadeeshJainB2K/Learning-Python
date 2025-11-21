x = float(input ("Enetr a number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

greatest = None 

if x>y and x >z : 
    greatest = x 
elif y>x and y>z :
    greatest = y
else :
    greatest = z

print ("Greatest among ", x , " , " , y , " and " , z , " is " , greatest )