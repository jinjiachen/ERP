#coding=cp936
#/usr/bin/env python

from __future__ import division
from math import pi
import math



def fun1(Pc,Di,fi,cigama,deltae):###�˹�ʽ��������Ͳ��ǿ��
#�жϹ�ʽ��ʤ��Χ
    if Pc<=0.4*cigama*fi:
        delta=Pc*Di/(2*cigama*fi-Pc)#Ͳ�����
        cigamat=Pc*(Di+deltae)/2/deltae
        if cigamat<=cigama*fi:
            return(1)
        else:
            return(0)
    else:
        return(2)#��ʽ�����÷���0

def fun2(a1,a2,a3):##�˺���������������Ӧ��
    if a1=='Q235B':#a1Ϊ���� a2Ϊ��� a3Ϊ�¶�
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
    elif a1=='�ֹ�20':
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

def fun3(D,S):##���������ƫ��
    if D<=102:#D�⾶ S���
        dev=max(0.125*S,0.4)
    else:
        if S/D<=0.05:dev=max(0.15*S,0.4)
        elif S/D<=0.1:dev=max(0.125*S,0.4)
        else:dev=max(0.1*S,0.4)
    return(dev)

def fun4(Pc,Di,fi,cigama,C,t):###�˹�ʽ���������ͷǿ��
    K=1
    deltah=K*Pc*Di/(2*cigama*fi-0.5*Pc)#��ͷ����
    if 0.87*t>(deltah+C):
        return(1)
    else:
        return(0)


def fun5(Di):##�����ͷ�ݻ�
    V=pi/24*Di**3+pi/4*Di**2*25
    V=V/1000**3
    return(V)

def fun6(D1,t1):##�����ͷ����
    m=7.85*pi*t1*(D1**2/3+5/6*D1*t1+2/3*t1**2+(D1+t1)*25)*10**-6
    return(m)


def fun7(Vc,Di):##����֪�ݻ����ھ�������¼�Բ�����賤��
    L=4*Vc/(pi*Di**2)*1000**3##VcΪԲ������ݻ�
    return(L)

def fun8(Di,t,L):##����Ͳ�������
    m=pi*(Di+t)*L*t/1000**3*7850
    return(m)

def fun9(Di,L):##����Ͳ���ݻ�
    Vs=pi/4*Di**2*L/1000**3#DiͲ���ھ�,LͲ�峤��,VsͲ���ݻ�
    return(Vs)

def fun10(do,deltant,Pc,Di,fi,cigama,mt1,mt2,t,tem,ou1,in1,deltae,cigama1,bra):###�˹����㿪�ײ�ǿ
    dop=do-2*deltant+2*(1+fun3(do,deltant))#do�ӹ��⾶deltant�ӹܱں�
    fr=fun2(mt2,deltant,tem)/fun2(mt1,t,tem)#�ӹܲ��ϵ�����Ӧ�������(Ͳ����ͷ)���ϵ�����Ӧ���ı�ֵ
    deltaet=deltant-1-fun3(do,deltant)#�ӹܵ���Ч���
    if fr>1:
        fr=1
    if bra=='Ͳ��':
        if Pc<=0.4*cigama*fi:#�жϹ�ʽ���÷�Χ
            delta=Pc*Di/(2*cigama*fi-Pc)#Ͳ�������
            A=dop*delta+2*delta*deltaet*(1-fr)#���貹ǿ���
    elif bra=='��Բ��ͷ':
        delta=0.9*Pc*Di/(2*cigama*fi-0.5*Pc)#��ͷ������,0.9Ϊϵ��K1
        A=dop*delta+2*delta*deltaet*(1-fr)#���貹ǿ���
#    elif bra=='ƽ�Ƿ�ͷ':
#        delta=
#        A=0.5*dop*deltap
    print A    
    B=max(2*dop,dop+2*t+2*deltant)#��Ч���
    h1=min(math.sqrt(dop*deltant),ou1)#��Ч�߶�
    h2=min(math.sqrt(dop*deltant),in1)#��Ч�߶�
    A1=(B-dop)*(deltae-delta)-2*deltaet*(deltae-delta)*(1-fr)
    print A1
    if Pc<=0.4*cigama1*fi:#�жϹ�ʽ���÷�Χ
        deltat=Pc*(do-2*deltant)/(2*cigama1*fi-Pc)#�ӹܼ�����
    A2=2*h1*(deltaet-deltat)*fr+2*h2*(deltaet-1)*fr
    print A2
    if A1+A2>A:
        return(1)
    else:
        return(0)
    
    
        
