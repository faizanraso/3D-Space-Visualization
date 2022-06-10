# Faizan Rasool, 400180032
# Python Version 3.8.9

import serial
import math

s = serial.Serial("COM4", 115200)
print("Opening: " +s.name)

file2 = open("DATA.xyz", 'a') //create or open file to store xyz coordiantes

file2.truncate(0) //empty the file before collecting values
x_dist = 0
displacement = 100

for i in range(1,321): # change to 321, 32 samples per rotation for 10 rotation
    if(i==33 or i == 65 or i == 97 or i == 129 or i == 161 or i == 193 or i==225 or i==257 or i==289 or i==321):
        x_dist += displacement

    temp = s.readline() # retrive data from ToF sensor
    data = temp.decode() # decode it to save as string
    data = data.replace("0","") # remove all values expect the distance measurement
    data = data.replace(" ","")
    data = data.replace(",","")
    
    data = float(data)
    angle = (2*math.pi*((i%32)* 11.25))/360 # calculate angle
    y_dist = data*math.sin(angle) # determine y component
    z_dist = data*math.cos(angle) # determine x component

    dataToSubmit = str(str(int(x_dist)) + ", " + str(int(y_dist)) + ", " + str(int(z_dist)) + "\n")
    print(dataToSubmit) # print data for user

    file2.write('{} {} {}\n'.format(x_dist,y_dist,z_dist))

s.close() # close serial
file2.close()


