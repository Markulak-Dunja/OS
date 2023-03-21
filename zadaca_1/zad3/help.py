import sys
from math import cos, sin, pi

def point_on_circle(center,radius):
    #za velike kazaljke od 3pi/2 do 7pi/2 i 45 veličina 
    #za male 0 do 2pi veličine 30
    angle = 3*pi/2
    angle1 = 0
    radius1 = 30
    i = 0
    with open('filename.txt', 'w') as f:
        sys.stdout = f 
        while (angle<7*pi/2):
            x = center[0] + (radius * cos(angle))
            y = center[1] + (radius * sin(angle))
            angle += pi / 30
            #angle += pi/12 
            
            #print("if(i=",i,"){")
            print("do Sys.wait(550);")
            print("do Screen.setColor(false);")
            print("do Screen.drawLine(x1,y1,x2,y2);")
            print("do Screen.setColor(true);")
            print("do Screen.drawLine(x11,y11,x22,y22);")
            print("let x2 = ", round(x),";")
            print("let y2 = ",round(y),";")
            print("do Screen.drawLine(x1,y1,x2,y2);")
            print("do Screen.drawCircle(265,150,2);")
            i = i+1

            if (i==30):
                x1 = center[0] + (radius1 * cos(angle1))
                y1 = center[1] + (radius1* sin(angle1))
                angle1 += pi / 6
                print("do Screen.setColor(false);")
                print("do Screen.drawLine(x11,y11,x22,y22);")
                print("do Screen.setColor(true);")
                print("let x22 = ", round(x1),";")
                print("let y22 = ",round(y1),";")
                print("do Screen.drawLine(x11,y11,x22,y22);")
                print("do Screen.drawCircle(265,150,2);")

                i = 0

        

    return x,y



(x,y) = point_on_circle([265,150],45)
