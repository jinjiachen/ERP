# -*- coding: cp936 -*-
#/usr/bin/env python

import wx
import math
import fun
import create_excel


class VolumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'压力容器',(10,10),(700,700))
        self.panel=wx.Panel(self)
        type=['已知参数','未知条件']
        mat1=['钢管20','Q245R']
        self.singlebox=wx.RadioBox(self.panel,-1,'请选择类型',choices=type)
        #################创建初始界面
        #开始创建筒体和封头的界面
        self.input10=wx.Choice(self.panel,-1,(120,200),choices=mat1)#切换条件时所需
        self.input11=wx.TextCtrl(self.panel,-1,'',(120,240))
        self.button2=wx.Button(self.panel,-1,'确定',(120,440))
        self.button2.Show(False)
        self.input10.Show(False)
        self.input11.Show(False)
        
        self.text1=wx.StaticText(self.panel,-1,'容器容积(m^3)',(20,80))
        self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
        self.text2=wx.StaticText(self.panel,-1,'设计压力(MPa)',(20,120))
        self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
        self.text3=wx.StaticText(self.panel,-1,'设计温度(℃)',(20,160))
        self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
        self.text4=wx.StaticText(self.panel,-1,'焊接系数',(20,200))
        self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
        self.text5=wx.StaticText(self.panel,-1,'筒体材料',(20,240))
        self.input5=wx.Choice(self.panel,-1,(120,240),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'筒体内径(mm)',(20,280))
        self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
        self.text7=wx.StaticText(self.panel,-1,'筒体壁厚(mm)',(20,320))
        self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
        self.text8=wx.StaticText(self.panel,-1,'封头内径(mm)',(20,360))
        self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
        self.text9=wx.StaticText(self.panel,-1,'封头壁厚(mm)',(20,400))
        self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))
        self.button1=wx.Button(self.panel,-1,'确定',(120,440))
        #筒体和封头界面结束

        self.Bind(wx.EVT_RADIOBOX,self.GetIndex,self.singlebox)#单选按钮的事件
        self.Bind(wx.EVT_BUTTON,self.fun1,self.button1)#按钮1的事件
        self.Bind(wx.EVT_BUTTON,self.fun2,self.button2)#按钮2的事件
        self.Bind(wx.EVT_CHOICE,self.renew1,self.input5)#第一个下拉选择的更新事件
        self.Bind(wx.EVT_CHOICE,self.renew2,self.input10)#第二个下拉选择的更新事件

        #开始创建开孔补强界面
        list1=['无','筒体','椭圆封头']
        list2=['钢管20','Q245R']
        self.singlebox1=wx.RadioBox(self.panel,-1,'开孔补强位置',choices=list1,pos=(400,0))
        self.text21=wx.StaticText(self.panel,-1,'接管外径(mm)',(400,80))
        self.input21=wx.TextCtrl(self.panel,-1,'',(500,80))
        self.text22=wx.StaticText(self.panel,-1,'接管壁厚(mm)',(400,120))
        self.input22=wx.TextCtrl(self.panel,-1,'',(500,120))
        self.text23=wx.StaticText(self.panel,-1,'接管材料',(400,160))
        self.input23=wx.Choice(self.panel,-1,(500,160),choices=list2)
        self.text24=wx.StaticText(self.panel,-1,'外伸长度(mm)',(400,200))
        self.input24=wx.TextCtrl(self.panel,-1,'',(500,200))
        self.text25=wx.StaticText(self.panel,-1,'内伸长度(mm)',(400,240))
        self.input25=wx.TextCtrl(self.panel,-1,'',(500,240))
        button3=wx.Button(self.panel,-1,'计算(等面积补强法)',(400,280))
        #开孔补强界面结束

        #初始化
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
            
        self.Bind(wx.EVT_BUTTON,self.fun3,button3)#计算开孔补强事件
        self.Bind(wx.EVT_RADIOBOX,self.renew4,self.singlebox1)#对开孔界面进行更新

        #鞍式支座界面的创建
        list3=['有垫板的鞍式支座','无垫板的鞍式支座']
        self.singlebox2=wx.RadioBox(self.panel,-1,'鞍式支座类型',choices=list3,pos=(400,320))
        self.text26=wx.StaticText(self.panel,-1,'腹板(mm)',(400,400))
        self.input26=wx.TextCtrl(self.panel,-1,'',(500,400))
        self.text27=wx.StaticText(self.panel,-1,'筋板(mm)',(400,440))
        self.input27=wx.TextCtrl(self.panel,-1,'',(500,440))
        self.text28=wx.StaticText(self.panel,-1,'底板(mm)',(400,480))
        self.input28=wx.TextCtrl(self.panel,-1,'',(500,480))
        self.text29=wx.StaticText(self.panel,-1,'垫板(mm)',(400,520))
        self.input29=wx.TextCtrl(self.panel,-1,'',(500,520))
        #界面创建结束
        
        self.Bind(wx.EVT_RADIOBOX,self.renew3,self.singlebox2)#更新垫板事件

        #########写入excel
        final=wx.Button(self.panel,-1,'输出到excel',(400,560))
        self.Bind(wx.EVT_BUTTON,self.wtexl,final)
        

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

            self.input4.Show(True)
            self.input5.Show(True)
            self.input10.Show(False)
            self.input11.Show(False)
            self.button2.Show(False)
            self.button1.Show(True)


        elif self.singlebox.GetSelection()==1:            
            self.text1.SetLabel('设计压力(MPa)')
            self.text2.SetLabel('设计温度(℃)')
            self.text3.SetLabel('焊接系数')
            self.text4.SetLabel('筒体材料')
            self.text5.SetLabel('筒体内径(mm)')
            self.text6.SetLabel('筒体壁厚(mm)')
            self.text7.SetLabel('筒体长度(mm)')
            self.text8.SetLabel('封头内径(mm)')
            self.text9.SetLabel('封头壁厚(mm)')
            if self.input10.GetStringSelection()=='Q245R':
                self.text5.SetLabel('筒体内径(mm)')
                self.text8.SetLabel('封头内径(mm)')
            else:
                self.text5.SetLabel('筒体外径(mm)')
                self.text8.SetLabel('封头外径(mm)')
            
            self.input4.Show(False)
            self.input5.Show(False)
            self.input10.Show(True)
            self.input11.Show(True)
            self.button1.Show(False)
            self.button2.Show(True)
            
            
            

    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('cp936')
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
#        print V
        L=fun.fun7(float(self.input1.GetValue())-2*V,Di)
#        print L
        m=fun.fun8(Di,t,L)
#        print m

    def fun2(self,event):
        test=self.input10.GetStringSelection().encode('cp936')
        Pc=float(self.input1.GetValue())#设计压力
        tem=float(self.input2.GetValue())#设计温度
        fi=float(self.input3.GetValue())#焊接系数
        t=float(self.input6.GetValue())#筒体壁厚
        L=float(self.input7.GetValue())#筒体长度
        t1=float(self.input9.GetValue())#封头厚度
        cigama=fun.fun2(test,t,tem)#筒体的材料许用应力
        if test=='Q245R':
            C=1.3
            Di=float(self.input11.GetValue())#筒体内径
            D1=float(self.input8.GetValue())#封头的内径
        else:
            D=float(self.input11.GetValue())#筒体外径
            S=float(self.input6.GetValue())#筒体壁厚
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

#        print fun.fun9(Di,L)+2*fun.fun5(D1)

    def fun3(self,event):
        do=float(self.input21.GetValue())#接管外径
        deltant=float(self.input22.GetValue())#接管壁厚
        mt2=self.input23.GetStringSelection().encode('cp936')#接管的材料
        ou1=float(self.input24.GetValue())#接管外伸长度
        in1=float(self.input25.GetValue())#接管内伸长度
        if self.singlebox.GetSelection()==0:#不同的选项对应不同的参数
            test=self.input5.GetStringSelection().encode('cp936')
            Pc=float(self.input2.GetValue())#设计压力
            tem=float(self.input3.GetValue())#设计温度
            fi=float(self.input4.GetValue())#焊接系数
            t=float(self.input7.GetValue())#筒体壁厚
            t1=float(self.input9.GetValue())#封头厚度
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
        elif self.singlebox.GetSelection()==1:
            test=self.input10.GetStringSelection().encode('cp936')
            Pc=float(self.input1.GetValue())#设计压力
            tem=float(self.input2.GetValue())#设计温度
            fi=float(self.input3.GetValue())#焊接系数
            t=float(self.input6.GetValue())#筒体壁厚
            L=float(self.input7.GetValue())#筒体长度
            t1=float(self.input9.GetValue())#封头厚度
            cigama=fun.fun2(test,t,tem)#筒体的材料许用应力
            if test=='Q245R':
                C=1.3
                Di=float(self.input11.GetValue())#筒体内径
                D1=float(self.input8.GetValue())#封头的内径
            else:
                D=float(self.input11.GetValue())#筒体外径
                S=float(self.input6.GetValue())#筒体壁厚
                C1=fun.fun3(D,S)#筒体材料下偏差
                C=1+C1
                Di=D-2*t#当材料为钢管20时筒体的内径
                D1=float(self.input8.GetValue())-2*t1#封头为EHB时的内径
            deltae=t-C#筒体的有效厚度
        cigama1=fun.fun2(mt2,deltant,tem)#接管在设计温度下的许用应力
        bra=self.singlebox1.GetStringSelection().encode('cp936')
        if bra=='筒体':
            result=fun.fun10(do,deltant,Pc,Di,fi,cigama,test,mt2,t,tem,ou1,in1,deltae,cigama1,bra)
        elif bra=='椭圆封头':
            result=fun.fun10(do,deltant,Pc,D1,fi,fun.fun2('Q245R',t1,tem),'Q245R',mt2,t1,tem,ou1,in1,(t1-1.3),cigama1,bra)
        if result==1:
            wx.MessageBox('开孔补强满足强度要求!','信息',style=wx.OK)
        
        
        
    def renew1(self,event):#当选择不同的材料时，更新对应的标签
        if self.input5.GetStringSelection().encode('cp936')=='钢管20':
            self.text6.SetLabel('筒体外径(mm)')
            self.text8.SetLabel('封头外径(mm)')
        else:
            self.text6.SetLabel('筒体内径(mm)')
            self.text8.SetLabel('封头内径(mm)')

    def renew2(self,event):#当选择不同的材料时，更新对应的标签
        if self.input10.GetStringSelection().encode('cp936')=='钢管20':
            self.text5.SetLabel('筒体外径(mm)')
            self.text8.SetLabel('封头外径(mm)')
        else:
            self.text5.SetLabel('筒体内径(mm)')
            self.text8.SetLabel('封头内径(mm)')

    def renew3(self,event):#更新垫板
        if self.singlebox2.GetSelection()==1:
            self.text29.Disable()
            self.input29.Disable()
        else:
            self.text29.Enable()
            self.input29.Enable()

    def renew4(self,event):#更新开孔界面
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

    def wtexl(self,event):#写入excel
        if self.singlebox.GetSelection()==0:#不同的选项对应不同的参数
            test=self.input5.GetStringSelection().encode('cp936')
            Pc=float(self.input2.GetValue())#设计压力
            tem=float(self.input3.GetValue())#设计温度
            fi=float(self.input4.GetValue())#焊接系数
            t=float(self.input7.GetValue())#筒体壁厚
            t1=float(self.input9.GetValue())#封头厚度
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
        elif self.singlebox.GetSelection()==1:
            test=self.input10.GetStringSelection().encode('cp936')
            Pc=float(self.input1.GetValue())#设计压力
            tem=float(self.input2.GetValue())#设计温度
            fi=float(self.input3.GetValue())#焊接系数
            t=float(self.input6.GetValue())#筒体壁厚
            L=float(self.input7.GetValue())#筒体长度
            t1=float(self.input9.GetValue())#封头厚度
            cigama=fun.fun2(test,t,tem)#筒体的材料许用应力
            if test=='Q245R':
                C=1.3
                Di=float(self.input11.GetValue())#筒体内径
                D1=float(self.input8.GetValue())#封头的内径
            else:
                D=float(self.input11.GetValue())#筒体外径
                S=float(self.input6.GetValue())#筒体壁厚
                C1=fun.fun3(D,S)#筒体材料下偏差
                C=1+C1
                Di=D-2*t#当材料为钢管20时筒体的内径
                D1=float(self.input8.GetValue())-2*t1#封头为EHB时的内径
            deltae=t-C#筒体的有效厚度
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

