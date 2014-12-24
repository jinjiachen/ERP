#/usr/bin/env python
#coding=utf-8

import wx
import math
import fun

pi=3.14159265357

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
            self.text1.Show(False)
            self.text2.Show(False)
            self.text3.Show(False)
            self.text4.Show(False)
            self.text5.Show(False)
            self.text6.Show(False)
            self.text7.Show(False)
            self.text8.Show(False)
            self.text9.Show(False)
            self.input1.Show(False)
            self.input2.Show(False)
            self.input3.Show(False)
            self.input4.Show(False)
            self.input5.Show(False)
            self.input6.Show(False)
            self.input7.Show(False)
            self.input8.Show(False)
            self.input9.Show(False)

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
            

        elif self.singlebox.GetSelection()==1:
            self.text1.Show(True)
            self.text2.Show(True)
            self.text3.Show(True)
            self.text4.Show(True)
            self.text5.Show(True)
            self.text6.Show(True)
            self.text7.Show(True)
            self.text8.Show(True)
            self.text9.Show(True)
            self.input1.Show(True)
            self.input2.Show(True)
            self.input3.Show(True)
            self.input4.Show(True)
            self.input5.Show(True)
            self.input6.Show(True)
            self.input7.Show(True)
            self.input8.Show(True)
            self.input9.Show(True)
            
            self.text4.SetLabel('筒体的长度(mm)')
            self.text5.SetLabel('筒体的直径(mm)')
            self.text6.SetLabel('筒体的壁厚(mm)')
            self.text7.SetLabel('封头的尺寸(mm)')
            self.text8.SetLabel('封头壁厚(mm)')
            self.text9.SetLabel('容器的容积(m^3)')

    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('utf-8')
        print type(test)
        if test=='Q245R':
            C=1.3
        else:
            D=float(self.input6.GetValue())
            S=float(self.input7.GetValue())
            C1=fun.fun3(D,S)
            C=1+C1
        Pc=float(self.input2.GetValue())
        fi=float(self.input4.GetValue())
        t=float(self.input7.GetValue())
        tem=float(self.input3.GetValue())
        cigama=fun.fun2(test,t,tem)
        deltae=t-C
        Di=float(self.input6.GetValue())
        result=fun.fun1(Pc,Di,fi,cigama,deltae,C,t)
        if result==3:
            wx.MessageBox('筒体强度不满足!','警告',style=wx.OK)
        elif result==4:
            wx.MessageBox('封头强度不满足!','警告',style=wx.OK)
        elif result==5:
            wx.MessageBox('筒体封头强度通过!','验证',style=wx.OK)
        elif result==2:
            wx.MessageBox('筒体和封头的强度都不满足!',style=wx.OK)
        elif result==0:
            wx.MessageBox('公式不适用','警告',style=wx.OK)
            

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
