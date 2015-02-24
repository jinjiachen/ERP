#/usr/bin/env python
#coding=utf-8

import wx
##import wx.lib.scrolledpanel as scrolled
import math
import fun


class HeatTransferFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'换热器',(10,10),(700,700))
        self.panel=wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 800,900)
        type1=['容积未知','容积已知']
        type2=['圆筒直径D≤600','圆筒直径D>600']
        type3=['胀接','焊接']
        mat1=['钢管20','Q245R']
        mat2=['Q245R','Q345R']
        mat3=['T2','TP2']
        ############开始创建壳体计算的界面
        self.singlebox1=wx.RadioBox(self.panel,-1,'请选择类型',choices=type1)
        self.text1=wx.StaticText(self.panel,-1,'壳程设计压力(MPa)',(20,70))
        self.input1=wx.TextCtrl(self.panel,-1,'',(130,70))
        self.text2=wx.StaticText(self.panel,-1,'壳程设计温度(℃)',(20,110))
        self.input2=wx.TextCtrl(self.panel,-1,'',(130,110))
        self.text3=wx.StaticText(self.panel,-1,'焊接系数',(20,150))
        self.input3=wx.TextCtrl(self.panel,-1,'',(130,150))
        self.text4=wx.StaticText(self.panel,-1,'壳侧腐蚀余量(mm)',(20,190))
        self.input4=wx.TextCtrl(self.panel,-1,'',(130,190))        
        self.text5=wx.StaticText(self.panel,-1,'筒体材料',(20,230))
        self.input5=wx.Choice(self.panel,-1,(130,230),choices=mat1)
        self.text6=wx.StaticText(self.panel,-1,'筒体内径(mm)',(20,270))
        self.input6=wx.TextCtrl(self.panel,-1,'',(130,270))
        self.text7=wx.StaticText(self.panel,-1,'筒体壁厚(mm)',(20,310))
        self.input7=wx.TextCtrl(self.panel,-1,'',(130,310))
        self.text8=wx.StaticText(self.panel,-1,'筒体长度(mm)',(20,350))
        self.input8=wx.TextCtrl(self.panel,-1,'',(130,350))
        self.button1=wx.Button(self.panel,-1,'计算筒体强度(内压)',(20,390))
        ##############创建结束

        self.Bind(wx.EVT_CHOICE,self.renew1,self.input5)#选择不同壳体材料时的更新
        self.Bind(wx.EVT_BUTTON,self.fun1,self.button1)#按钮1的事件


        ########创建左管箱计算界面
        self.text31=wx.StaticText(self.panel,-1,'管程设计压力(MPa)',(350,70))
        self.input31=wx.TextCtrl(self.panel,-1,'',(500,70))
        self.text32=wx.StaticText(self.panel,-1,'管程设计温度(℃)',(350,110))
        self.input32=wx.TextCtrl(self.panel,-1,'',(500,110))
        self.text33=wx.StaticText(self.panel,-1,'焊接系数',(350,150))
        self.input33=wx.TextCtrl(self.panel,-1,'',(500,150))
        self.text34=wx.StaticText(self.panel,-1,'管侧腐蚀余量(mm)',(350,190))
        self.input34=wx.TextCtrl(self.panel,-1,'',(500,190))        
        self.text35=wx.StaticText(self.panel,-1,'管箱筒体材料',(350,230))
        self.input35=wx.Choice(self.panel,-1,(500,230),choices=mat1)
        self.text36=wx.StaticText(self.panel,-1,'管箱筒体内径(mm)',(350,270))
        self.input36=wx.TextCtrl(self.panel,-1,'',(500,270))
        self.text37=wx.StaticText(self.panel,-1,'管箱筒体壁厚(mm)',(350,310))
        self.input37=wx.TextCtrl(self.panel,-1,'',(500,310))
        self.text38=wx.StaticText(self.panel,-1,'左管箱筒体长度(mm)',(350,350))
        self.input38=wx.TextCtrl(self.panel,-1,'',(500,350))
        self.text39=wx.StaticText(self.panel,-1,'右管箱筒体长度(mm)',(350,390))
        self.input39=wx.TextCtrl(self.panel,-1,'',(500,390))        
        self.button2=wx.Button(self.panel,-1,'计算筒体强度(内压)',(350,430))        
        #创建结束


        ################开始创建管板计算界面
        self.singlebox2=wx.RadioBox(self.panel,-1,'钢制管板强度计算',(700,0),choices=type2)
        if self.singlebox2.GetSelection()==0:
            self.text10=wx.StaticText(self.panel,-1,'设计压力(MPa)',(700,70))
            self.input10=wx.TextCtrl(self.panel,-1,'',(850,70))
            self.text11=wx.StaticText(self.panel,-1,'管板外径(mm)',(700,110))
            self.input11=wx.TextCtrl(self.panel,-1,'',(850,110))
            self.text12=wx.StaticText(self.panel,-1,'管板名义厚度(mm)',(700,150))
            self.input12=wx.TextCtrl(self.panel,-1,'',(850,150))
            self.text13=wx.StaticText(self.panel,-1,'管板材料',(700,190))
            self.input13=wx.Choice(self.panel,-1,(850,190),choices=mat2)            
            self.text14=wx.StaticText(self.panel,-1,'管孔直径(mm)',(700,230))
            self.input14=wx.TextCtrl(self.panel,-1,'',(850,230))
            self.text15=wx.StaticText(self.panel,-1,'壳侧腐蚀余量(mm)',(700,270))
            self.input15=wx.TextCtrl(self.panel,-1,'',(850,270))                    
            self.text16=wx.StaticText(self.panel,-1,'管侧腐蚀余量(mm)',(700,310))
            self.input16=wx.TextCtrl(self.panel,-1,'',(850,310))
            self.text17=wx.StaticText(self.panel,-1,'壳侧结构开槽深度(mm)',(700,350))
            self.input17=wx.TextCtrl(self.panel,-1,'',(850,350))
            self.text18=wx.StaticText(self.panel,-1,'管侧分程隔板槽深度(mm)',(700,390))
            self.input18=wx.TextCtrl(self.panel,-1,'',(850,390))
            self.text19=wx.StaticText(self.panel,-1,'管板最小厚度(mm)',(700,430))
            self.input19=wx.TextCtrl(self.panel,-1,'',(850,430))
            self.text20=wx.StaticText(self.panel,-1,'管板与换热管连接形式',(700,470))
            self.input20=wx.Choice(self.panel,-1,(850,470),choices=type3)            
            self.text21=wx.StaticText(self.panel,-1,'一根管子支撑截面积(mm2)',(700,510))
            self.input21=wx.TextCtrl(self.panel,-1,'',(850,510))
            self.text22=wx.StaticText(self.panel,-1,'系数C(表20)',(700,550))
            self.input22=wx.TextCtrl(self.panel,-1,'',(850,550))
            self.text23=wx.StaticText(self.panel,-1,'有效焊接高度(mm)',(700,590))
            self.input23=wx.TextCtrl(self.panel,-1,'',(850,590))
            self.text2=wx.StaticText(self.panel,-1,'换热管材料',(700,630))
            self.input24=wx.Choice(self.panel,-1,(850,630),choices=mat3) 
            self.text25=wx.StaticText(self.panel,-1,'换热管长度(mm)',(700,670))
            self.input25=wx.TextCtrl(self.panel,-1,'',(850,670))
            self.text25=wx.StaticText(self.panel,-1,'换热管外径(mm)',(700,710))
            self.input25=wx.TextCtrl(self.panel,-1,'',(850,710))
            self.text25=wx.StaticText(self.panel,-1,'换热管壁厚(mm)',(700,750))
            self.input25=wx.TextCtrl(self.panel,-1,'',(850,750))
            self.text26=wx.StaticText(self.panel,-1,'支撑间距(mm)',(700,790))
            self.input26=wx.TextCtrl(self.panel,-1,'',(850,790))
            self.text27=wx.StaticText(self.panel,-1,'设计温度(℃)',(700,830))
            self.input27=wx.TextCtrl(self.panel,-1,'',(850,830))
            self.button3=wx.Button(self.panel,-1,'计算管板强度',(700,870))
            #创建结束

            self.Bind(wx.EVT_BUTTON,self.fun2,self.button3)##管板强度计算的事件驱动
            



    def fun1(self,event):
        test=self.input5.GetStringSelection().encode('cp936')
        Pc=float(self.input1.GetValue())#壳体设计压力
        tem=float(self.input2.GetValue())#壳体设计温度
        fi=float(self.input3.GetValue())#焊接系数
        C2=float(self.input4.GetValue())#腐蚀余量
        t=float(self.input7.GetValue())#筒体壁厚
        cigama=fun.fun2(test,t,tem)#筒体的材料许用应力
        if test=='Q245R':
            Di=float(self.input6.GetValue())#筒体内径
            C=0.3+C2
        else:
            D=float(self.input6.GetValue())#筒体外径
            S=float(self.input7.GetValue())#筒体壁厚
            C1=fun.fun3(D,S)#筒体材料下偏差
            C=C1+C2
            Di=D-2*t#当材料为钢管20时筒体的内径
        deltae=t-C#筒体的有效厚度
        result1=fun.fun1(Pc,Di,fi,cigama,deltae)#筒体计算强度回返值
        if result1==1:
            wx.MessageBox('筒体强度满足!','信息',style=wx.OK)
        elif result1==0:
            wx.MessageBox('筒体强度不满足!','警告',style=wx.OK)
        elif result1==2:
            wx.MessageBox('公式不适用','警告',style=wx.OK)


    def fun2(self,event):#管板的计算
        d=self.input14.GetValue()#管孔直径
        delta1=fun.fun11(d)#有管束部分的管板计算厚度
        deltan=self.input12.GetValue()#管板的名义厚度
        tem=self.input27.GetValue()#设计温度
        if self.input20.GetSelection()==0:
            S=fun.fun12(deltan,d)#最小管孔中心距
            Pc=self.input10.GetValue()#设计压力
            F=self.input21.GetValue()#管子所围成面积
            W=fun.fun18(Pc,F)#一根管子所支撑的载荷
            d0=self.input25.GetValue()#换热管外径
            cigamat1=fun.fun13(W,deltan,d0)#胀接时钢制管板与管子的接触应力
            t=self.input25.GetValue()#管子壁厚
            cigamat2=fun.fun19(W,d0,t)#管子的应力值
        l=self.input26.GetValue()#支撑间距
        C=self.input22.GetValue()#系数
        material=self.input13.GetStringSelection()#管板材料
        cigamat=fun.fun2(material,deltan,tem)#管板材料的许用应力
        delta2=fun.fun16(l,Pc,C,cigamat)#管板无管束部分的计算厚度
        C2=self.input15.GetValue()#壳徎腐蚀余量
        p=fun.fun17(C,cigamat,deltan,C2,l)#管板许用应力校核
        


    def renew1(self,event):#当选择不同的材料时，更新对应的标签
        if self.input5.GetStringSelection().encode('cp936')=='钢管20':
            self.text6.SetLabel('筒体外径(mm)')
        else:
            self.text6.SetLabel('筒体内径(mm)')


        

   
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=HeatTransferFrame()
    frame.Show()
    myapp.MainLoop()
