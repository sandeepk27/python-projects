# drawing circles using turtle

from turtle import *

speed(60)
bgcolor('black')
color('orange')
hideturtle()

n=1
p=True

while True:
    circle(n)
    if p:
        n=n-1
    else:
        n=n+1
    
    if n==0 or n==120:
        p = not p
    
    left(1)
    
done()