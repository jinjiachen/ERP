#coding=cp936
#/usr/bin/env python

from __future__ import division
from math import pi
import math



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

def fun2(a1,a2,a3):##此函数用来计算许用应力,按照标准NB/T47012-2010
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
    elif a1=='钢管20':
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
    elif a1=='Q345R':
        if a2>=3 and a2<16:
            if a3<=150:
                ans=170
            elif a3>150 and a3<200:
                ans=170+(165-170)/50*(a3-150)
        elif a2>=16 and a2<36:
            if a3<=100:
                ans=167
            elif a3>100 and a3<=150:
                ans=167+(165-167)/50*(a3-100)
            elif a3>150 and a3<=200:
                ans=165+(163-165)/50*(a3-150)
        elif a2>=36 and a2<60:
            if a3<=100:
                ans=163
            elif a3>100 and a3<=150:
                ans=163+(156-163)/50*(a3-100)
            elif a3>150 and a3<=200:
                ans=156+(144-156)/50*(a3-150)
    return(ans)

def fun3(D,S):##计算材料下偏差
    if D<=102:#D外径 S厚度
        dev=max(0.125*S,0.4)
    else:
        if S/D<=0.05:dev=max(0.15*S,0.4)
        elif S/D<=0.1:dev=max(0.125*S,0.4)
        else:dev=max(0.1*S,0.4)
    return(dev)

def fun4(Pc,Di,fi,cigama,C,t):###此公式用来计算封头强度
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

def fun9(Di,L):##计算筒体容积
    Vs=pi/4*Di**2*L/1000**3#Di筒体内径,L筒体长度,Vs筒体容积
    return(Vs)

def fun10(do,deltant,Pc,Di,fi,cigama,mt1,mt2,t,tem,ou1,in1,deltae,cigama1,bra):###此公计算开孔补强
    dop=do-2*deltant+2*(1+fun3(do,deltant))#do接管外径deltant接管壁厚
    fr=fun2(mt2,deltant,tem)/fun2(mt1,t,tem)#接管材料的许用应力与壳体(筒体或封头)材料的许用应力的比值
    deltaet=deltant-1-fun3(do,deltant)#接管的有效厚度
    if fr>1:
        fr=1
    if bra=='筒体':
        if Pc<=0.4*cigama*fi:#判断公式适用范围
            delta=Pc*Di/(2*cigama*fi-Pc)#筒体计算厚度
            A=dop*delta+2*delta*deltaet*(1-fr)#所需补强面积
    elif bra=='椭圆封头':
        delta=0.9*Pc*Di/(2*cigama*fi-0.5*Pc)#封头计算厚度,0.9为系数K1
        A=dop*delta+2*delta*deltaet*(1-fr)#所需补强面积
    print A    
    B=max(2*dop,dop+2*t+2*deltant)#有效宽度
    h1=min(math.sqrt(dop*deltant),ou1)#有效高度
    h2=min(math.sqrt(dop*deltant),in1)#有效高度
    A1=(B-dop)*(deltae-delta)-2*deltaet*(deltae-delta)*(1-fr)
    print A1
    if Pc<=0.4*cigama1*fi:#判断公式适用范围
        deltat=Pc*(do-2*deltant)/(2*cigama1*fi-Pc)#接管计算厚度
    A2=2*h1*(deltaet-deltat)*fr+2*h2*(deltaet-1)*fr
    print A2
    if A1+A2>A:
        return(1)
    else:
        return(0)
    
    
        
def fun11(d):###钢制管板的计算厚度
    d=float(d)#管孔直径
    delta=8+d/12
    return(delta)

def fun12(deltan,d):###胀接时，钢制管板管孔最小中心距
    deltan=float(deltan)#管板名义厚度
    d=float(d)#管孔直径
    s=(1+2.8/deltan)*d
    return(s)

def fun13(W,deltan,d0):###胀接时，管子与管板的接触应力
    W=float(W)#一根管子所支撑的载荷
    d0=float(d0)#管子外径
    deltan=float(deltan)#管板名义厚度
    cigamat=W/(3.14*d0*deltan)
    return(cigamat)

def fun14(W,d0,l):###焊接时，管子与管板接触面的剪切应力
    W=float(W)#一根管子所支撑的载荷
    d0=float(d0)#管子外径
    l=float(l)#管子与管板的有效焊接高度
    cigamat=W/(3.14*d0*l)
    return(cigamat)

def fun15(W,A):###作用于管子上的应力值
    W=float(W)#一根管子所支撑的载荷
    A=float(A)#管子的截面积
    cigamat=1.1*W/A
    return(cigamat)

def fun16(l,Pc,C,cigamat):###管板无管束部分的计算厚度
    l=float(l)#支撑的间距
    Pc=float(Pc)#设计压力
    C=float(C)#表20的系数
    delta=l*math.sqrt(Pc/C/cigamat)
    return(delta)

def fun17(C,cigamat,deltan,C2,l):###管板无管束部分许用应力校核
    C=float(C)#表20的系数
    deltan=float(deltan)#管板名义厚度
    C2=float(C2)##腐蚀余量
    l=float(l)#支撑的间距
    p=C*cigamat*(deltan-C2)**2/l**2
    return(p)

def fun18(Pc,F):###计算一根管子所支撑的载荷
    Pc=float(Pc)#设计压力
    F=float(F)#所围成的面积
    W=Pc*F
    return(W)

def fun19(W,d0,t):###管子的应力值
    d0=float(d0)#管子外径
    t=float(t)#管子壁厚
    di=d0-2*t
    A=math.pi/4*(d0**2-di**2)
    cigamat=1.1*W/A
    return(cigama)
