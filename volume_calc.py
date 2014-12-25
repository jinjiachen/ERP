#/usr/bin/env python
#coding=cp936

import wx
import math
import fun


class VolumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'ѹ������')
        self.panel=wx.Panel(self)
        type=['��֪����','δ֪����']
        self.singlebox=wx.RadioBox(self.panel,-1,'��ѡ������',choices=type)
        #������ʼ����
        self.text1=wx.StaticText(self.panel,-1,'�����ݻ�(m^3)',(20,80))
        self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
        self.text2=wx.StaticText(self.panel,-1,'���ѹ��(MPa)',(20,120))
        self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
        self.text3=wx.StaticText(self.panel,-1,'����¶�(��)',(20,160))
        self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
        self.text4=wx.StaticText(self.panel,-1,'����ϵ��',(20,200))
        self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
        self.text5=wx.StaticText(self.panel,-1,'Ͳ�����',(20,240))
        mat1=['�ֹ�20','Q245R']
        self.input5=wx.Choice(self.panel,-1,(120,240),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'Ͳ���ھ�(mm)',(20,280))
        self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
        self.text7=wx.StaticText(self.panel,-1,'Ͳ��ں�(mm)',(20,320))
        self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
        self.text8=wx.StaticText(self.panel,-1,'��ͷ�ھ�(mm)',(20,360))
        self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
        self.text9=wx.StaticText(self.panel,-1,'��ͷ�ں�(mm)',(20,400))
        self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))
        button=wx.Button(self.panel,-1,'ȷ��',(120,440))


        self.Bind(wx.EVT_RADIOBOX,self.GetIndex,self.singlebox)
        self.Bind(wx.EVT_BUTTON,self.fun1,button)
        self.Bind(wx.EVT_CHOICE,self.renew,self.input5)

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


                

            

        elif self.singlebox.GetSelection()==1:
            
            self.text4.SetLabel('Ͳ��ĳ���(mm)')
            self.text5.SetLabel('Ͳ���ֱ��(mm)')
            self.text6.SetLabel('Ͳ��ıں�(mm)')
            self.text7.SetLabel('��ͷ�ĳߴ�(mm)')
            self.text8.SetLabel('��ͷ�ں�(mm)')
            self.text9.SetLabel('�������ݻ�(m^3)')

    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('utf-8')
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
        print V
        L=fun.fun7(float(self.input1.GetValue())-2*V,Di)
        print L
        m=fun.fun8(Di,t,L)
        print m

    def renew(self,event):
        if self.input5.GetStringSelection().encode('cp936')=='�ֹ�20':
            self.text6.SetLabel('Ͳ���⾶(mm)')
            self.text8.SetLabel('��ͷ�⾶(mm)')
        else:
            self.text6.SetLabel('Ͳ���ھ�(mm)')
            self.text8.SetLabel('��ͷ�ھ�(mm)')
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=VolumeFrame()
    frame.Show()
    myapp.MainLoop()
