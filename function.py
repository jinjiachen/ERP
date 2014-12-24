#/usr/bin/env python
#coding=utf-8
from __future__ import division

#输入计算参数
Pc=input('请输入计算压力(MPa)\n')
Di=input('请输入筒体内径(mm)\n')
fi=input('请输入焊接系数\n')
cigama=input('请输入该材料在设计温度下的许用应力(MPa)\n')

#判断公式优胜范围
if Pc<=0.4*cigama*fi:
    delta=Pc*Di/(2*cigama*fi-Pc)#筒体计算
    print("筒体的计算厚度为:")
    print float(delta)

    K=1
    deltah=K*Pc*Di/(2*cigama*fi-0.5*Pc)#封头计算
    print('椭圆封头的计算厚度为:')
    print float(deltah)
else:
    print '公式不适用'




####################许用应力计算#########################
a1='钢管20'
a2=input('厚度\n')
a3=input('温度\n')
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
print ans



############材料下偏差##########
D=input('外径')
S=input('厚度')
if D<=102:
    dev=max(0.125*S,0.4)
else:
    if S/D<=0.05:dev=max(0.15*S,0.4)
    elif S/D<=0.1:dev=max(0.125*S,0.4)
    else:dev=max(0.1*S,0.4)
print dev


