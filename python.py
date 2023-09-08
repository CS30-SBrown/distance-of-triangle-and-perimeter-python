#ask for the number points to find the triangle
num1X = float(input("enter x of A: "))
num1Y = float(input("enter y of A: "))
num2X = float(input("enter x of B: "))
num2Y = float(input("enter y of B: "))
num3X = float(input("enter x of C: "))
num3Y = float(input("enter Y of C: "))

#function that calculates the distance between the entered points
def dist (X1,Y1,X2,Y2):
    distance = ((X2 - X1)**2+ (Y2 - Y1)**2)**0.5     
    return distance  

#save the distance of the sides            
sideAB = dist(num1X,num1Y,num2X,num2Y)
sideAC = dist(num1X,num1Y,num3X,num3Y)
sideBC = dist(num2X,num2Y,num3X,num3Y)

#display the information and calc the perimeter
print("SIDE LENGTHS & PERIMETER")
print("side AB =",sideAB)
print("side AC =",sideAC)
print("side BC =",sideBC)
print("perimeter is ",sideAB + sideAC + sideBC)
