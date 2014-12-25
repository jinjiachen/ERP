#/usr/bin/env python
#coding=cp936

import wx
import math
import fun


class VolumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'压力容器')
        self.panel=wx.Panel(self)
        type=['已知参数','未知条件']
        self.singlebox=wx.RadioBox(self.panel,-1,'请选择类型',choices=type)
        #创建初始界面
        self.text1=wx.StaticText(self.panel,-1,'容器容积(m^3)',(20,80))
        self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
        self.text2=wx.StaticText(self.panel,-1,'设计压力(MPa)',(20,120))
        self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
        self.text3=wx.StaticText(self.panel,-1,'设计温度(℃)',(20,160))
        self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
        self.text4=wx.StaticText(self.panel,-1,'焊接系数',(20,200))
        self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
        self.text5=wx.StaticText(self.panel,-1,'筒体材料',(20,240))
        mat1=['钢管20','Q245R']
        self.input5=wx.Choice(self.panel,-1,(120,240),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'筒体内径(mm)',(20,280))
        self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
        self.text7=wx.StaticText(self.panel,-1,'筒体壁厚(mm)',(20,320))
        self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
        self.text8=wx.StaticText(self.panel,-1,'封头内径(mm)',(20,360))
        self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
        self.text9=wx.StaticText(self.panel,-1,'封头壁厚(mm)',(20,400))
        self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))
        button=wx.Button(self.panel,-1,'确定',(120,440))


        self.Bind(wx.EVT_RADIOBOX,self.GetIndex,self.singlebox)
        self.Bind(wx.EVT_BUTTON,self.fun1,button)
        self.Bind(wx.EVT_CHOICE,self.renew,self.input5)

    def GetIndex(self,event):
        if self.singlebox.GetSelection()==0:#不同的选项对应不同的参数
            self.text1.SetLabel('容器容积(m^3)')
            self.text2.SetLabel('设计压力(MPa)')
            self.text3.SetLabel('设计温度(℃)')
            self.text4.SetLabel('焊接系数')
            self.text5.SetLabel('筒体材料')
            self.text7.SetLabel('筒体壁厚(mm)')
            self.text9.SetLabel('封头壁厚(mm)')
            if self.input5.GetStringSelection()=='Q245R':
                self.text6.SetLabel('筒体内径(mm)')
                self.text8.SetLabel('封头内径(mm)')
            else:
                self.text6.SetLabel('筒体外径(mm)')
                self.text8.SetLabel('封头外径(mm)')


                

            

        elif self.singlebox.GetSelection()==1:
            
            self.text4.SetLabel('筒体的长度(mm)')
            self.text5.SetLabel('筒体的直径(mm)')
            self.text6.SetLabel('筒体的壁厚(mm)')
            self.text7.SetLabel('封头的尺寸(mm)')
            self.text8.SetLabel('封头壁厚(mm)')
            self.text9.SetLabel('容器的容积(m^3)')

    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('utf-8')
        Pc=float(self.input2.GetValue())#设计压力
        fi=float(self.input4.GetValue())#焊接系数
        t=float(self.input7.GetValue())#筒体壁厚
        t1=float(self.input9.GetValue())#封头厚度
        tem=float(self.input3.GetValue())#设计温度
        cigama=fun.fun2(test,t,tem)#筒体的材料许用应力
        if test=='Q245R':
            C=1.3
            Di=float(self.input6.GetValue())#筒体内径
            D1=float(self.input8.GetValue())#封头的内径
        else:
            D=float(self.input6.GetValue())#筒体外径
            S=float(self.input7.GetValue())#筒体壁厚
            C1=fun.fun3(D,S)#筒体材料下偏差
            C=1+C1
            Di=D-2*t#当材料为钢管20时筒体的内径
            D1=float(self.input8.GetValue())-2*t1#封头为EHB时的内径
        deltae=t-C#筒体的有效厚度
        result1=fun.fun1(Pc,Di,fi,cigama,deltae)#筒体计算强度回返值
        result2=fun.fun4(Pc,D1,fi,fun.fun2('Q245R',t1,tem),1.3,t1)#封头强度计算返回值
        if result1==1 and result2:
            wx.MessageBox('筒体和封头强度满足!','信息',style=wx.OK)
        elif result1==0 and result2==0:
            wx.MessageBox('筒体和封头强度都不满足!','警告',style=wx.OK)
        elif result1==0:
            wx.MessageBox('筒体强度不满足!','警告',style=wx.OK)
        elif result2==0:
            wx.MessageBox('封头强度不满足!','警告',style=wx.OK)
        elif result1==2:
            wx.MessageBox('公式不适用','警告',style=wx.OK)
        
        V=fun.fun5(D1)
        print V
        L=fun.fun7(float(self.input1.GetValue())-2*V,Di)
        print L
        m=fun.fun8(Di,t,L)
        print m

    def renew(self,event):
        if self.input5.GetStringSelection().encode('cp936')=='钢管20':
            self.text6.SetLabel('筒体外径(mm)')
            self.text8.SetLabel('封头外径(mm)')
        else:
            self.text6.SetLabel('筒体内径(mm)')
            self.text8.SetLabel('封头内径(mm)')
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=VolumeFrame()
    frame.Show()
    myapp.MainLoop()
