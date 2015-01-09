# -*- coding: cp936 -*-
#/usr/bin/env python

import wx
import math
import fun
import create_excel


class VolumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'ѹ������',(10,10),(700,700))
        self.panel=wx.Panel(self)
        type=['��֪����','δ֪����']
        mat1=['�ֹ�20','Q245R']
        self.singlebox=wx.RadioBox(self.panel,-1,'��ѡ������',choices=type)
        #################������ʼ����
        #��ʼ����Ͳ��ͷ�ͷ�Ľ���
        self.input10=wx.Choice(self.panel,-1,(120,200),choices=mat1)#�л�����ʱ����
        self.input11=wx.TextCtrl(self.panel,-1,'',(120,240))
        self.button2=wx.Button(self.panel,-1,'ȷ��',(120,440))
        self.button2.Show(False)
        self.input10.Show(False)
        self.input11.Show(False)
        
        self.text1=wx.StaticText(self.panel,-1,'�����ݻ�(m^3)',(20,80))
        self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
        self.text2=wx.StaticText(self.panel,-1,'���ѹ��(MPa)',(20,120))
        self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
        self.text3=wx.StaticText(self.panel,-1,'����¶�(��)',(20,160))
        self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
        self.text4=wx.StaticText(self.panel,-1,'����ϵ��',(20,200))
        self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
        self.text5=wx.StaticText(self.panel,-1,'Ͳ�����',(20,240))
        self.input5=wx.Choice(self.panel,-1,(120,240),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'Ͳ���ھ�(mm)',(20,280))
        self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
        self.text7=wx.StaticText(self.panel,-1,'Ͳ��ں�(mm)',(20,320))
        self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
        self.text8=wx.StaticText(self.panel,-1,'��ͷ�ھ�(mm)',(20,360))
        self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
        self.text9=wx.StaticText(self.panel,-1,'��ͷ�ں�(mm)',(20,400))
        self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))
        self.button1=wx.Button(self.panel,-1,'ȷ��',(120,440))
        #Ͳ��ͷ�ͷ�������

        self.Bind(wx.EVT_RADIOBOX,self.GetIndex,self.singlebox)#��ѡ��ť���¼�
        self.Bind(wx.EVT_BUTTON,self.fun1,self.button1)#��ť1���¼�
        self.Bind(wx.EVT_BUTTON,self.fun2,self.button2)#��ť2���¼�
        self.Bind(wx.EVT_CHOICE,self.renew1,self.input5)#��һ������ѡ��ĸ����¼�
        self.Bind(wx.EVT_CHOICE,self.renew2,self.input10)#�ڶ�������ѡ��ĸ����¼�

        #��ʼ�������ײ�ǿ����
        list1=['��','Ͳ��','��Բ��ͷ']
        list2=['�ֹ�20','Q245R']
        self.singlebox1=wx.RadioBox(self.panel,-1,'���ײ�ǿλ��',choices=list1,pos=(400,0))
        self.text21=wx.StaticText(self.panel,-1,'�ӹ��⾶(mm)',(400,80))
        self.input21=wx.TextCtrl(self.panel,-1,'',(500,80))
        self.text22=wx.StaticText(self.panel,-1,'�ӹܱں�(mm)',(400,120))
        self.input22=wx.TextCtrl(self.panel,-1,'',(500,120))
        self.text23=wx.StaticText(self.panel,-1,'�ӹܲ���',(400,160))
        self.input23=wx.Choice(self.panel,-1,(500,160),choices=list2)
        self.text24=wx.StaticText(self.panel,-1,'���쳤��(mm)',(400,200))
        self.input24=wx.TextCtrl(self.panel,-1,'',(500,200))
        self.text25=wx.StaticText(self.panel,-1,'���쳤��(mm)',(400,240))
        self.input25=wx.TextCtrl(self.panel,-1,'',(500,240))
        button3=wx.Button(self.panel,-1,'����(�������ǿ��)',(400,280))
        #���ײ�ǿ�������

        #��ʼ��
        self.text21.Disable()
        self.text22.Disable()
        self.text23.Disable()
        self.text24.Disable()
        self.text25.Disable()
        self.input21.Disable()
        self.input22.Disable()
        self.input23.Disable()
        self.input24.Disable()
        self.input25.Disable()
            
        self.Bind(wx.EVT_BUTTON,self.fun3,button3)#���㿪�ײ�ǿ�¼�
        self.Bind(wx.EVT_RADIOBOX,self.renew4,self.singlebox1)#�Կ��׽�����и���

        #��ʽ֧������Ĵ���
        list3=['�е��İ�ʽ֧��','�޵��İ�ʽ֧��']
        self.singlebox2=wx.RadioBox(self.panel,-1,'��ʽ֧������',choices=list3,pos=(400,320))
        self.text26=wx.StaticText(self.panel,-1,'����(mm)',(400,400))
        self.input26=wx.TextCtrl(self.panel,-1,'',(500,400))
        self.text27=wx.StaticText(self.panel,-1,'���(mm)',(400,440))
        self.input27=wx.TextCtrl(self.panel,-1,'',(500,440))
        self.text28=wx.StaticText(self.panel,-1,'�װ�(mm)',(400,480))
        self.input28=wx.TextCtrl(self.panel,-1,'',(500,480))
        self.text29=wx.StaticText(self.panel,-1,'���(mm)',(400,520))
        self.input29=wx.TextCtrl(self.panel,-1,'',(500,520))
        #���洴������
        
        self.Bind(wx.EVT_RADIOBOX,self.renew3,self.singlebox2)#���µ���¼�

        #########д��excel
        final=wx.Button(self.panel,-1,'�����excel',(400,560))
        self.Bind(wx.EVT_BUTTON,self.wtexl,final)
        

    def GetIndex(self,event):        
        if self.singlebox.GetSelection()==0:#��ͬ��ѡ���Ӧ��ͬ�Ĳ���
            self.text1.SetLabel('�����ݻ�(m^3)')
            self.text2.SetLabel('���ѹ��(MPa)')
            self.text3.SetLabel('����¶�(��)')
            self.text4.SetLabel('����ϵ��')
            self.text5.SetLabel('Ͳ�����')
            self.text7.SetLabel('Ͳ��ں�(mm)')
            self.text9.SetLabel('��ͷ�ں�(mm)')
            if self.input5.GetStringSelection()=='Q245R':
                self.text6.SetLabel('Ͳ���ھ�(mm)')
                self.text8.SetLabel('��ͷ�ھ�(mm)')
            else:
                self.text6.SetLabel('Ͳ���⾶(mm)')
                self.text8.SetLabel('��ͷ�⾶(mm)')

            self.input4.Show(True)
            self.input5.Show(True)
            self.input10.Show(False)
            self.input11.Show(False)
            self.button2.Show(False)
            self.button1.Show(True)


        elif self.singlebox.GetSelection()==1:            
            self.text1.SetLabel('���ѹ��(MPa)')
            self.text2.SetLabel('����¶�(��)')
            self.text3.SetLabel('����ϵ��')
            self.text4.SetLabel('Ͳ�����')
            self.text5.SetLabel('Ͳ���ھ�(mm)')
            self.text6.SetLabel('Ͳ��ں�(mm)')
            self.text7.SetLabel('Ͳ�峤��(mm)')
            self.text8.SetLabel('��ͷ�ھ�(mm)')
            self.text9.SetLabel('��ͷ�ں�(mm)')
            if self.input10.GetStringSelection()=='Q245R':
                self.text5.SetLabel('Ͳ���ھ�(mm)')
                self.text8.SetLabel('��ͷ�ھ�(mm)')
            else:
                self.text5.SetLabel('Ͳ���⾶(mm)')
                self.text8.SetLabel('��ͷ�⾶(mm)')
            
            self.input4.Show(False)
            self.input5.Show(False)
            self.input10.Show(True)
            self.input11.Show(True)
            self.button1.Show(False)
            self.button2.Show(True)
            
            
            

    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('cp936')
        Pc=float(self.input2.GetValue())#���ѹ��
        fi=float(self.input4.GetValue())#����ϵ��
        t=float(self.input7.GetValue())#Ͳ��ں�
        t1=float(self.input9.GetValue())#��ͷ���
        tem=float(self.input3.GetValue())#����¶�
        cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
        if test=='Q245R':
            C=1.3
            Di=float(self.input6.GetValue())#Ͳ���ھ�
            D1=float(self.input8.GetValue())#��ͷ���ھ�
        else:
            D=float(self.input6.GetValue())#Ͳ���⾶
            S=float(self.input7.GetValue())#Ͳ��ں�
            C1=fun.fun3(D,S)#Ͳ�������ƫ��
            C=1+C1
            Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
            D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
        deltae=t-C#Ͳ�����Ч���
        result1=fun.fun1(Pc,Di,fi,cigama,deltae)#Ͳ�����ǿ�Ȼط�ֵ
        result2=fun.fun4(Pc,D1,fi,fun.fun2('Q245R',t1,tem),1.3,t1)#��ͷǿ�ȼ��㷵��ֵ
        if result1==1 and result2:
            wx.MessageBox('Ͳ��ͷ�ͷǿ������!','��Ϣ',style=wx.OK)
        elif result1==0 and result2==0:
            wx.MessageBox('Ͳ��ͷ�ͷǿ�ȶ�������!','����',style=wx.OK)
        elif result1==0:
            wx.MessageBox('Ͳ��ǿ�Ȳ�����!','����',style=wx.OK)
        elif result2==0:
            wx.MessageBox('��ͷǿ�Ȳ�����!','����',style=wx.OK)
        elif result1==2:
            wx.MessageBox('��ʽ������','����',style=wx.OK)
        
        V=fun.fun5(D1)
#        print V
        L=fun.fun7(float(self.input1.GetValue())-2*V,Di)
#        print L
        m=fun.fun8(Di,t,L)
#        print m

    def fun2(self,event):
        test=self.input10.GetStringSelection().encode('cp936')
        Pc=float(self.input1.GetValue())#���ѹ��
        tem=float(self.input2.GetValue())#����¶�
        fi=float(self.input3.GetValue())#����ϵ��
        t=float(self.input6.GetValue())#Ͳ��ں�
        L=float(self.input7.GetValue())#Ͳ�峤��
        t1=float(self.input9.GetValue())#��ͷ���
        cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
        if test=='Q245R':
            C=1.3
            Di=float(self.input11.GetValue())#Ͳ���ھ�
            D1=float(self.input8.GetValue())#��ͷ���ھ�
        else:
            D=float(self.input11.GetValue())#Ͳ���⾶
            S=float(self.input6.GetValue())#Ͳ��ں�
            C1=fun.fun3(D,S)#Ͳ�������ƫ��
            C=1+C1
            Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
            D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
        deltae=t-C#Ͳ�����Ч���
        result1=fun.fun1(Pc,Di,fi,cigama,deltae)#Ͳ�����ǿ�Ȼط�ֵ
        result2=fun.fun4(Pc,D1,fi,fun.fun2('Q245R',t1,tem),1.3,t1)#��ͷǿ�ȼ��㷵��ֵ
        if result1==1 and result2:
            wx.MessageBox('Ͳ��ͷ�ͷǿ������!','��Ϣ',style=wx.OK)
        elif result1==0 and result2==0:
            wx.MessageBox('Ͳ��ͷ�ͷǿ�ȶ�������!','����',style=wx.OK)
        elif result1==0:
            wx.MessageBox('Ͳ��ǿ�Ȳ�����!','����',style=wx.OK)
        elif result2==0:
            wx.MessageBox('��ͷǿ�Ȳ�����!','����',style=wx.OK)
        elif result1==2:
            wx.MessageBox('��ʽ������','����',style=wx.OK)

#        print fun.fun9(Di,L)+2*fun.fun5(D1)

    def fun3(self,event):
        do=float(self.input21.GetValue())#�ӹ��⾶
        deltant=float(self.input22.GetValue())#�ӹܱں�
        mt2=self.input23.GetStringSelection().encode('cp936')#�ӹܵĲ���
        ou1=float(self.input24.GetValue())#�ӹ����쳤��
        in1=float(self.input25.GetValue())#�ӹ����쳤��
        if self.singlebox.GetSelection()==0:#��ͬ��ѡ���Ӧ��ͬ�Ĳ���
            test=self.input5.GetStringSelection().encode('cp936')
            Pc=float(self.input2.GetValue())#���ѹ��
            tem=float(self.input3.GetValue())#����¶�
            fi=float(self.input4.GetValue())#����ϵ��
            t=float(self.input7.GetValue())#Ͳ��ں�
            t1=float(self.input9.GetValue())#��ͷ���
            cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
            if test=='Q245R':
                C=1.3
                Di=float(self.input6.GetValue())#Ͳ���ھ�
                D1=float(self.input8.GetValue())#��ͷ���ھ�
            else:
                D=float(self.input6.GetValue())#Ͳ���⾶
                S=float(self.input7.GetValue())#Ͳ��ں�
                C1=fun.fun3(D,S)#Ͳ�������ƫ��
                C=1+C1
                Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
                D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
            deltae=t-C#Ͳ�����Ч���
        elif self.singlebox.GetSelection()==1:
            test=self.input10.GetStringSelection().encode('cp936')
            Pc=float(self.input1.GetValue())#���ѹ��
            tem=float(self.input2.GetValue())#����¶�
            fi=float(self.input3.GetValue())#����ϵ��
            t=float(self.input6.GetValue())#Ͳ��ں�
            L=float(self.input7.GetValue())#Ͳ�峤��
            t1=float(self.input9.GetValue())#��ͷ���
            cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
            if test=='Q245R':
                C=1.3
                Di=float(self.input11.GetValue())#Ͳ���ھ�
                D1=float(self.input8.GetValue())#��ͷ���ھ�
            else:
                D=float(self.input11.GetValue())#Ͳ���⾶
                S=float(self.input6.GetValue())#Ͳ��ں�
                C1=fun.fun3(D,S)#Ͳ�������ƫ��
                C=1+C1
                Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
                D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
            deltae=t-C#Ͳ�����Ч���
        cigama1=fun.fun2(mt2,deltant,tem)#�ӹ�������¶��µ�����Ӧ��
        bra=self.singlebox1.GetStringSelection().encode('cp936')
        if bra=='Ͳ��':
            result=fun.fun10(do,deltant,Pc,Di,fi,cigama,test,mt2,t,tem,ou1,in1,deltae,cigama1,bra)
        elif bra=='��Բ��ͷ':
            result=fun.fun10(do,deltant,Pc,D1,fi,fun.fun2('Q245R',t1,tem),'Q245R',mt2,t1,tem,ou1,in1,(t1-1.3),cigama1,bra)
        if result==1:
            wx.MessageBox('���ײ�ǿ����ǿ��Ҫ��!','��Ϣ',style=wx.OK)
        
        
        
    def renew1(self,event):#��ѡ��ͬ�Ĳ���ʱ�����¶�Ӧ�ı�ǩ
        if self.input5.GetStringSelection().encode('cp936')=='�ֹ�20':
            self.text6.SetLabel('Ͳ���⾶(mm)')
            self.text8.SetLabel('��ͷ�⾶(mm)')
        else:
            self.text6.SetLabel('Ͳ���ھ�(mm)')
            self.text8.SetLabel('��ͷ�ھ�(mm)')

    def renew2(self,event):#��ѡ��ͬ�Ĳ���ʱ�����¶�Ӧ�ı�ǩ
        if self.input10.GetStringSelection().encode('cp936')=='�ֹ�20':
            self.text5.SetLabel('Ͳ���⾶(mm)')
            self.text8.SetLabel('��ͷ�⾶(mm)')
        else:
            self.text5.SetLabel('Ͳ���ھ�(mm)')
            self.text8.SetLabel('��ͷ�ھ�(mm)')

    def renew3(self,event):#���µ��
        if self.singlebox2.GetSelection()==1:
            self.text29.Disable()
            self.input29.Disable()
        else:
            self.text29.Enable()
            self.input29.Enable()

    def renew4(self,event):#���¿��׽���
        if self.singlebox1.GetSelection()==0:
            self.text21.Disable()
            self.text22.Disable()
            self.text23.Disable()
            self.text24.Disable()
            self.text25.Disable()
            self.input21.Disable()
            self.input22.Disable()
            self.input23.Disable()
            self.input24.Disable()
            self.input25.Disable()
        else:
            self.text21.Enable()
            self.text22.Enable()
            self.text23.Enable()
            self.text24.Enable()
            self.text25.Enable()
            self.input21.Enable()
            self.input22.Enable()
            self.input23.Enable()
            self.input24.Enable()
            self.input25.Enable()

    def wtexl(self,event):#д��excel
        if self.singlebox.GetSelection()==0:#��ͬ��ѡ���Ӧ��ͬ�Ĳ���
            test=self.input5.GetStringSelection().encode('cp936')
            Pc=float(self.input2.GetValue())#���ѹ��
            tem=float(self.input3.GetValue())#����¶�
            fi=float(self.input4.GetValue())#����ϵ��
            t=float(self.input7.GetValue())#Ͳ��ں�
            t1=float(self.input9.GetValue())#��ͷ���
            cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
            if test=='Q245R':
                C=1.3
                Di=float(self.input6.GetValue())#Ͳ���ھ�
                D1=float(self.input8.GetValue())#��ͷ���ھ�
            else:
                D=float(self.input6.GetValue())#Ͳ���⾶
                S=float(self.input7.GetValue())#Ͳ��ں�
                C1=fun.fun3(D,S)#Ͳ�������ƫ��
                C=1+C1
                Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
                D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
            deltae=t-C#Ͳ�����Ч���
        elif self.singlebox.GetSelection()==1:
            test=self.input10.GetStringSelection().encode('cp936')
            Pc=float(self.input1.GetValue())#���ѹ��
            tem=float(self.input2.GetValue())#����¶�
            fi=float(self.input3.GetValue())#����ϵ��
            t=float(self.input6.GetValue())#Ͳ��ں�
            L=float(self.input7.GetValue())#Ͳ�峤��
            t1=float(self.input9.GetValue())#��ͷ���
            cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
            if test=='Q245R':
                C=1.3
                Di=float(self.input11.GetValue())#Ͳ���ھ�
                D1=float(self.input8.GetValue())#��ͷ���ھ�
            else:
                D=float(self.input11.GetValue())#Ͳ���⾶
                S=float(self.input6.GetValue())#Ͳ��ں�
                C1=fun.fun3(D,S)#Ͳ�������ƫ��
                C=1+C1
                Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
                D1=float(self.input8.GetValue())-2*t1#��ͷΪEHBʱ���ھ�
            deltae=t-C#Ͳ�����Ч���
        x3=self.text26.GetLabel()
        x4=self.text27.GetLabel()
        x5=self.text28.GetLabel()
        x6=self.input23.GetStringSelection()
        create_excel.exc(self.input10.GetStringSelection(),fun.fun8(Di,t,L),fun.fun6(D1,t1),x3,x4,x5,x6)
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=VolumeFrame()
    frame.Show()
    myapp.MainLoop()

