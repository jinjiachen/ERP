#/usr/bin/env python
#coding=utf-8


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


