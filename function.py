#/usr/bin/env python
#coding=utf-8


#����������
Pc=input('���������ѹ��(MPa)\n')
Di=input('������Ͳ���ھ�(mm)\n')
fi=input('�����뺸��ϵ��\n')
cigama=input('������ò���������¶��µ�����Ӧ��(MPa)\n')

#�жϹ�ʽ��ʤ��Χ
if Pc<=0.4*cigama*fi:
    delta=Pc*Di/(2*cigama*fi-Pc)#Ͳ�����
    print("Ͳ��ļ�����Ϊ:")
    print float(delta)

    K=1
    deltah=K*Pc*Di/(2*cigama*fi-0.5*Pc)#��ͷ����
    print('��Բ��ͷ�ļ�����Ϊ:')
    print float(deltah)
else:
    print '��ʽ������'


