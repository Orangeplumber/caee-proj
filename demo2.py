# -*- coding: utf-8 -*-
from math import *
def f1(w1):
    return w1

def f2(w2):
    return w2

def f3(th1,th2,w1,w2,g,l1,l2,m1,m2):
    x=(-1)*g*(2*m1+m2)*sin(th1)-(m2*g*sin(th1-(2*th2)))-(2*sin(th1-th2)*m2*((w2**2*l2)+(w1**2*l1*cos(th1-th2))))/(l1*(2*m1+m2-m2*cos((2*th1)-(2*th2))))
    # x=w1
    return x

def f4(th1,th2,w1,w2,g,l1,l2,m1,m2):
    x=(2*sin(th1-th2)*(pow(w1,2)*l1*(m1+m2)+g*(m1+m2)*cos(th1)+pow(w2,2)*l2*m2*cos(th1-th2)))/(l2*(2*m1+m2-m2*cos(2*th1-2*th2)))
    return x 
 
def rk4(th10, th20, w10,w20, h,n, m1,m2,l1,l2,g):
    t = [0] * (n + 1)
    th1_lis = [0] * (n + 1)
    th2_lis = [0] * (n + 1)
    w1_lis= [0] * (n + 1)
    w2_lis= [0] * (n + 1)
    t[0] = x = 0
    th1_lis[0]=th1=th10
    th2_lis[0]=th2=th20
    w1_lis[0]=w1=w10
    w2_lis[0]=w2=w20
    for i in range(1, n + 1):
        k11 = h * f1(w1)
        k12 = h * f2(w2)
        k13 = h * f3(th1,th2,w1,w2,g,l1,l2,m1,m2)
        k14 = h * f4(th1,th2,w1,w2,g,l1,l2,m1,m2)

        k21 = h * f1(w1+0.5*h*k13)
        k22 = h * f2(w2+0.5*h*k14)
        k23 = h * f3(th1+0.5*h*k11,th2+0.5*h*k12,w1+0.5*h*k13,w2+0.5*h*k14,g,l1,l2,m1,m2)
        k24 = h * f4(th1+0.5*h*k11,th2+0.5*h*k12,w1+0.5*h*k13,w2+0.5*h*k14,g,l1,l2,m1,m2)

        k31 = h * f1(w1+0.5*h*k23)
        k32 = h * f2(w1+0.5*h*k24)
        k33 = h * f3(th1+0.5*h*k21,th2+0.5*h*k22,w1+0.5*h*k23,w2+0.5*h*k24,g,l1,l2,m1,m2)
        k34 = h * f4(th1+0.5*h*k21,th2+0.5*h*k22,w1+0.5*h*k23,w2+0.5*h*k24,g,l1,l2,m1,m2)

        k41 = h * f1(w1+0.5*h*k33)
        k42 = h * f2(w1+0.5*h*k34)
        k43 = h * f3(th1+0.5*h*k31,th2+0.5*h*k32,w1+0.5*h*k33,w2+0.5*h*k34,g,l1,l2,m1,m2)
        k44 = h * f4(th1+0.5*h*k31,th2+0.5*h*k32,w1+0.5*h*k33,w2+0.5*h*k34,g,l1,l2,m1,m2)
        
        th1_lis[i]=th1=th1_lis[i-1]+(k11+2*k21+2*k31+k41)/6
        th2_lis[i]=th2=th2_lis[i-1]+(k12+2*k22+2*k32+k42)/6
        w1_lis[i]=w1=w1_lis[i-1]+(k13+2*k23+2*k33+k43)/6
        w2_lis[i]=w2=w2_lis[i-1]+(k11+2*k21+2*k31+k41)/6
        t[i] = x = t[0] + i * h
    return th1_lis,th2_lis,w1_lis,w2_lis
 
 
th1, th2, w1, w2 = rk4(0, 1, 0, 0,0.001,1000,1,1,1,1,9.80)
# for x, y in list(zip(vx, vy))[::1]:
#     print("%4.1f %10.5f %+12.4e" % (x, y, y - (4 + x * x)**2/16))

for i in range(1,100):
    print(th1[i])

