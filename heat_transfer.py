#/usr/bin/env python
#coding=cp936

import wx
##import wx.lib.scrolledpanel as scrolled
import math
import fun


class HeatTransferFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'������',(10,10),(700,700))
        self.panel=wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 800,800)
        type1=['�ݻ�δ֪','�ݻ���֪']
        type2=['ԲͲֱ��D��600','ԲͲֱ��D>600']
        type3=['�ͽ�','����']
        mat1=['�ֹ�20','Q245R']
        mat2=['Q245R','Q345R']
        mat3=['T2','TP2']
        ############��ʼ�����������Ľ���
        self.singlebox1=wx.RadioBox(self.panel,-1,'��ѡ������',choices=type1)
        self.text1=wx.StaticText(self.panel,-1,'�ǳ����ѹ��(MPa)',(20,70))
        self.input1=wx.TextCtrl(self.panel,-1,'',(130,70))
        self.text2=wx.StaticText(self.panel,-1,'�ǳ�����¶�(��)',(20,110))
        self.input2=wx.TextCtrl(self.panel,-1,'',(130,110))
        self.text3=wx.StaticText(self.panel,-1,'����ϵ��',(20,150))
        self.input3=wx.TextCtrl(self.panel,-1,'',(130,150))
        self.text4=wx.StaticText(self.panel,-1,'��ʴ����(mm)',(20,190))
        self.input4=wx.TextCtrl(self.panel,-1,'',(130,190))        
        self.text5=wx.StaticText(self.panel,-1,'Ͳ�����',(20,230))
        self.input5=wx.Choice(self.panel,-1,(130,230),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'Ͳ���ھ�(mm)',(20,270))
        self.input6=wx.TextCtrl(self.panel,-1,'',(130,270))
        self.text7=wx.StaticText(self.panel,-1,'Ͳ��ں�(mm)',(20,310))
        self.input7=wx.TextCtrl(self.panel,-1,'',(130,310))
        self.text8=wx.StaticText(self.panel,-1,'Ͳ�峤��(mm)',(20,350))
        self.input8=wx.TextCtrl(self.panel,-1,'',(130,350))
        self.button1=wx.Button(self.panel,-1,'����Ͳ��ǿ��(��ѹ)',(20,390))
        ##############��������

        self.Bind(wx.EVT_CHOICE,self.renew1,self.input5)#ѡ��ͬ�������ʱ�ĸ���
        self.Bind(wx.EVT_BUTTON,self.fun1,self.button1)#��ť1���¼�


        ################��ʼ�����ܰ�������
        self.singlebox2=wx.RadioBox(self.panel,-1,'���ƹܰ�ǿ�ȼ���',(350,0),choices=type2)
        if self.singlebox2.GetSelection()==0:
            self.text11=wx.StaticText(self.panel,-1,'�ܰ��⾶(mm)',(350,70))
            self.input11=wx.TextCtrl(self.panel,-1,'',(500,70))
            self.text12=wx.StaticText(self.panel,-1,'�ܰ�������(mm)',(350,110))
            self.input12=wx.TextCtrl(self.panel,-1,'',(500,110))
            self.text13=wx.StaticText(self.panel,-1,'�ܰ����',(350,150))
            self.input13=wx.Choice(self.panel,-1,(500,150),choices=mat2)            
            self.text14=wx.StaticText(self.panel,-1,'�ܿ�ֱ��(mm)',(350,190))
            self.input14=wx.TextCtrl(self.panel,-1,'',(500,190))
            self.text15=wx.StaticText(self.panel,-1,'�ǲฯʴ����(mm)',(350,230))
            self.input15=wx.TextCtrl(self.panel,-1,'',(500,230))                    
            self.text16=wx.StaticText(self.panel,-1,'�ܲฯʴ����(mm)',(350,270))
            self.input16=wx.TextCtrl(self.panel,-1,'',(500,270))
            self.text17=wx.StaticText(self.panel,-1,'�ǲ�ṹ�������(mm)',(350,310))
            self.input17=wx.TextCtrl(self.panel,-1,'',(500,310))
            self.text18=wx.StaticText(self.panel,-1,'�ܲ�̸ֳ�������(mm)',(350,350))
            self.input18=wx.TextCtrl(self.panel,-1,'',(500,350))
            self.text19=wx.StaticText(self.panel,-1,'�ܰ���С���(mm)',(350,390))
            self.input19=wx.TextCtrl(self.panel,-1,'',(500,390))
            self.text20=wx.StaticText(self.panel,-1,'�ܰ��뻻�ȹ�������ʽ',(350,430))
            self.input20=wx.Choice(self.panel,-1,(500,430),choices=type3)            
            self.text21=wx.StaticText(self.panel,-1,'һ������֧�Ž����(mm2)',(350,470))
            self.input21=wx.TextCtrl(self.panel,-1,'',(500,470))
            self.text22=wx.StaticText(self.panel,-1,'ϵ��C(��20)',(350,510))
            self.input22=wx.TextCtrl(self.panel,-1,'',(500,510))
            self.text23=wx.StaticText(self.panel,-1,'��Ч���Ӹ߶�(mm)',(350,550))
            self.input23=wx.TextCtrl(self.panel,-1,'',(500,550))
            self.text2=wx.StaticText(self.panel,-1,'���ȹܲ���',(350,590))
            self.input24=wx.Choice(self.panel,-1,(500,590),choices=mat3) 
            self.text25=wx.StaticText(self.panel,-1,'��Ч���Ӹ߶�(mm)',(350,630))
            self.input25=wx.TextCtrl(self.panel,-1,'',(500,630))
            self.text25=wx.StaticText(self.panel,-1,'���ȹ��⾶(mm)',(350,670))
            self.input25=wx.TextCtrl(self.panel,-1,'',(500,670))
            self.text25=wx.StaticText(self.panel,-1,'���ȹܱں�(mm)',(350,710))
            self.input25=wx.TextCtrl(self.panel,-1,'',(500,710))
            



    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('cp936')
        Pc=float(self.input1.GetValue())#�������ѹ��
        tem=float(self.input2.GetValue())#��������¶�
        fi=float(self.input3.GetValue())#����ϵ��
        C2=float(self.input4.GetValue())#��ʴ����
        t=float(self.input7.GetValue())#Ͳ��ں�
        cigama=fun.fun2(test,t,tem)#Ͳ��Ĳ�������Ӧ��
        if test=='Q245R':
            Di=float(self.input6.GetValue())#Ͳ���ھ�
            C=0.3+C2
        else:
            D=float(self.input6.GetValue())#Ͳ���⾶
            S=float(self.input7.GetValue())#Ͳ��ں�
            C1=fun.fun3(D,S)#Ͳ�������ƫ��
            C=C1+C2
            Di=D-2*t#������Ϊ�ֹ�20ʱͲ����ھ�
        deltae=t-C#Ͳ�����Ч���
        result1=fun.fun1(Pc,Di,fi,cigama,deltae)#Ͳ�����ǿ�Ȼط�ֵ
        if result1==1:
            wx.MessageBox('Ͳ��ǿ������!','��Ϣ',style=wx.OK)
        elif result1==0:
            wx.MessageBox('Ͳ��ǿ�Ȳ�����!','����',style=wx.OK)
        elif result1==2:
            wx.MessageBox('��ʽ������','����',style=wx.OK)



    def renew1(self,event):#��ѡ��ͬ�Ĳ���ʱ�����¶�Ӧ�ı�ǩ
        if self.input5.GetStringSelection().encode('cp936')=='�ֹ�20':
            self.text6.SetLabel('Ͳ���⾶(mm)')
        else:
            self.text6.SetLabel('Ͳ���ھ�(mm)')


        

   
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=HeatTransferFrame()
    frame.Show()
    myapp.MainLoop()
