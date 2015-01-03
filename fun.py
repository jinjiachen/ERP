#/usr/bin/env python
#coding=utf-8

from __future__ import division
from math import pi



def fun1(Pc,Di,fi,cigama,deltae):###此公式用来计算筒体强度
#判断公式优胜范围
    if Pc<=0.4*cigama*fi:
        delta=Pc*Di/(2*cigama*fi-Pc)#筒体计算
        cigamat=Pc*(Di+deltae)/2/deltae
        if cigamat<=cigama*fi:
            return(1)
        else:
            return(0)
    else:
        return(2)#公式不适用返回0

def fun2(a1,a2,a3):##此函数用来计算许用应力
    if a1=='Q235B':#a1为材料 a2为厚度 a3为温度
        if a2>=3 and a2<16:
            if a3<150:
                ans=113
            elif a3>=150 and a3<200:
                ans=(105-113)/50*(a3-150)+113
            elif a2>=16 and a2<30:
                if a3<100:
                    ans=113
                elif a3>=100 and a3<150:
                    ans=(107-113)/50*(a3-100)+113
                elif a3>=150 and a3<200:
                    ans=(99-107)/50*(a3-150)+107
    elif a1=='Q245R':
        if a2>=3 and a2<16:
            if a3<=20:
                ans=133
            elif a3>20 and a3<=100:
                ans=(132-133)/80*(a3-20)+133
            elif a3>100 and a3<=150:
                ans=(126-132)/50*(a3-100)+132
            elif a3>150 and a3<=200:
                ans=(118-126)/50*(a3-150)+126
        elif a2>=16 and a2<36:
            if a3<=20:
                ans=133
            elif a3>20 and a3<=100:
                ans=(126-133)/80*(a3-20)+133
            elif a3>100 and a3<=150:
                ans=(120-126)/50*(a3-100)+126
            elif a3>150 and a3<=200:
                ans=(112-120)/50*(a3-150)+120
        elif a2>=36 and a2<60:
            if a3<=20:
                ans=133
            elif a3>20 and a3<=100:
                ans=(120-133)/80*(a3-20)+133
            elif a3>100 and a3<=150:
                ans=(114-120)/50*(a3-100)+120
            elif a3>150 and a3<=200:
                ans=(107-114)/50*(a3-150)+114
    else:
        if a2<=10:
            if a3<=20:
                ans=137
            elif a3>20 and a3<=100:
                ans=(132-137)/80*(a3-20)+137
            elif a3>100 and a3<=150:
                ans=(126-132)/50*(a3-100)+132
            elif a3>150 and a3<=200:
                ans=(118-126)/50*(a3-150)+126
        if a2>10 and a2<=16:
            if a3<=20:
                ans=137
            elif a3>20 and a3<=100:
                ans=(132-137)/80*(a3-20)+137
            elif a3>100 and a3<=150:
                ans=(126-132)/50*(a3-100)+132
            elif a3>150 and a3<=200:
                ans=(118-126)/50*(a3-150)+126
    return(ans)

def fun3(D,S):##计算材料下偏差
    if D<=102:#D外径 S厚度
        dev=max(0.125*S,0.4)
    else:
        if S/D<=0.05:dev=max(0.15*S,0.4)
        elif S/D<=0.1:dev=max(0.125*S,0.4)
        else:dev=max(0.1*S,0.4)
    return(dev)

def fun4(Pc,Di,fi,cigama,C,t):###此公式用来计算筒体强度
    K=1
    deltah=K*Pc*Di/(2*cigama*fi-0.5*Pc)#封头计算
    if 0.87*t>(deltah+C):
        return(1)
    else:
        return(0)




def fun5(Di):##计算封头容积
    V=pi/24*Di**3+pi/4*Di**2*25
    V=V/1000**3
    return(V)

def fun6(D1,t1):##计算封头质量
    m=7.85*pi*t1*(D1**2/3+5/6*D1*t1+2/3*t1**2+(D1+t1)*25)*10**-6
    return(m)


def fun7(Vc,Di):##在已知容积和内径的情况下计圆柱所需长度
    L=4*Vc/(pi*Di**2)*1000**3##Vc为圆柱体的容积
    return(L)

def fun8(Di,t,L):##计算筒体的质量
    m=pi*(Di+t)*L*t/1000**3*7850
    return(m)
