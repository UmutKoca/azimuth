print("""
    Convert grads to degrees, find zone and calculate azimuth angle
""")

import math

X1 = float(input("Please enter X1 coordinate: "))
Y1 = float(input("Please enter Y1 coordinate: "))
X2 = float(input("Please enter X2 coordinate: "))
Y2 = float(input("Please enter Y2 coordinate: "))

def check_zone(X1,X2,Y1,Y2):
       
    deltaX = X2 - X1
    deltaY = Y2 - Y1

    if(deltaX != 0):
        delta = deltaY / deltaX
        azimuth_grad = math.atan(delta)*200 / math.pi
        azimuth_degree = azimuth_grad * 180 / 200

        distance = math.sqrt(deltaY**2 + deltaX**2)
    
        if(deltaY > 0 and deltaX > 0):
            print("Distance between points: " + str(distance))
            print("Angle is in First Zone")
            print("Azimuth angle in degree: " + str(azimuth_degree))
            print("Azimuth angle in grad: " + str(azimuth_grad))
            print("\n")

        if(deltaY > 0 and deltaX < 0):
            print("Distance between points: " + str(distance))
            print("Angle is in Second Zone")
            print("Azimuth angle in degree: "+ str(azimuth_degree + 180))
            print("Azimuth angle in grad: " + str(azimuth_grad + 200))
            print("\n")

        if(deltaY < 0 and deltaX < 0):
            print("Distance between points: " + str(distance))
            print("Angle is in Third Zone")
            print("Azimuth angle in degree: " + str(azimuth_degree + 180))
            print("Azimuth angle in grad: " + str(azimuth_grad + 200))
            print("\n")

        if(deltaY < 0 and deltaX > 0):
            print("Distance between points: " + str(distance))
            print("Angle is in Fourth Zone")
            print("Azimuth angle in degree: " + str(azimuth_degree + 360))
            print("Azimuht angle in grad: " + str(azimuth_grad + 400))
            print("\n")
    else:
        print("something wrong happened, please check the coordinates.")
        

print("Results for points: \n")
check_zone(X1,X2,Y1,Y2)





