#coding=cp936

import wx
import format


class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'材料定额生成器',size=(400,600))
        panel=wx.Panel(self)
        list1=['方钢板','圆钢板','钢管','圆钢','组合件']
        list2=['Q245R','Q235B','20']
        list3=['无','外购','ZY','ZY,无图','无图','外购,无图','需修改']
        wx.StaticText(panel,-1,'图号',(50,90))
        self.input1=wx.TextCtrl(panel,-1,'',(120,90))
        wx.StaticText(panel,-1,'名称',(50,130))
        self.input2=wx.TextCtrl(panel,-1,'',(120,130))
        wx.StaticText(panel,-1,'材料',(50,170))
        self.input3=wx.Choice(panel,-1,(120,170),choices=list1)
        self.text4=wx.StaticText(panel,-1,'牌号',(50,210))
        self.input4=wx.Choice(panel,-1,(120,210),choices=list2)
        self.text5=wx.StaticText(panel,-1,'长度(mm)',(50,250))
        self.input5=wx.TextCtrl(panel,-1,'',(120,250))
        self.text6=wx.StaticText(panel,-1,'宽度(mm)',(50,290))
        self.input6=wx.TextCtrl(panel,-1,'',(120,290))
        self.text7=wx.StaticText(panel,-1,'厚度(mm)',(50,330))
        self.input7=wx.TextCtrl(panel,-1,'',(120,330))
        wx.StaticText(panel,-1,'行号',(50,50))
        self.input8=wx.TextCtrl(panel,-1,'',(120,50))
        wx.StaticText(panel,-1,'数量',(50,370))
        self.input9=wx.TextCtrl(panel,-1,'',(120,370))
        self.input10=wx.RadioBox(panel,-1,'备注',(50,410),wx.DefaultSize,list3,3)
        button=wx.Button(panel,-1,'输出到表格',(50,520))
#        wx.CheckBox(panel,-1,'外购',pos=(50,410))
#        wx.CheckBox(panel,-1,'ZY',pos=(110,410))
#        wx.CheckBox(panel,-1,'ZY,无图',pos=(170,410))
#        wx.CheckBox(panel,-1,'无图',pos=(50,450))
#        wx.CheckBox(panel,-1,'需修改',pos=(110,450))
#        wx.CheckBox(panel,-1,'外购,无图',pos=(170,450))
        

        self.Bind(wx.EVT_BUTTON,self.fun1,button)
        self.Bind(wx.EVT_CHOICE,self.renew1,self.input3)


    def fun1(self,event):
        i=self.input8.GetValue()#行号
        num=self.input1.GetValue()#图号
        name=self.input2.GetValue()#名称
        mat=self.input3.GetStringSelection()#材料
        pai=self.input4.GetStringSelection()#牌号
        amount=float(self.input9.GetValue())#数量
        x1=self.input5.GetValue()
        x2=self.input6.GetValue()
        x3=self.input7.GetValue()
        PS=self.input10.GetStringSelection()#备注一栏
        format.exc(i,num,name,mat,pai,x1,x2,x3,amount,PS)



    def renew1(self,event):
        if self.input3.GetStringSelection().encode('cp936')=='钢管':
            self.text4.Enable()
            self.input4.Enable()
            self.text5.Enable()
            self.input5.Enable()
            self.text6.Enable()
            self.input6.Enable()
            self.input7.Enable()
            self.text7.Enable()
            self.text5.SetLabel('外径(mm)')
            self.text6.SetLabel('厚度(mm)')
            self.text7.SetLabel('长度(mm)')
        elif self.input3.GetStringSelection().encode('cp936')=='圆钢':
            self.text4.Enable()
            self.input4.Enable()
            self.text5.Enable()
            self.input5.Enable()
            self.text6.Enable()
            self.input6.Enable()
            self.text5.SetLabel('外径(mm)')
            self.text6.SetLabel('长度(mm)')
            self.text7.Disable()
            self.input7.Disable()
        elif self.input3.GetStringSelection().encode('cp936')=='方钢板':
            self.text4.Enable()
            self.input4.Enable()
            self.text5.Enable()
            self.input5.Enable()
            self.text6.Enable()
            self.input6.Enable()
            self.text7.Enable()
            self.input7.Enable()
            self.text5.SetLabel('长度(mm)')
            self.text6.SetLabel('宽度(mm)')
            self.text7.SetLabel('厚度(mm)')
        elif self.input3.GetStringSelection().encode('cp936')=='圆钢板':
            self.text4.Enable()
            self.input4.Enable()
            self.text5.Enable()
            self.input5.Enable()
            self.text6.Enable()
            self.input6.Enable()
            self.text5.SetLabel('外径(mm)')
            self.text6.SetLabel('厚度(mm)')
            self.text7.Disable()
            self.input7.Disable()
        elif self.input3.GetStringSelection().encode('cp936')=='组合件':
            self.text4.Disable()
            self.input4.Disable()
            self.text5.Disable()
            self.input5.Disable()
            self.text6.Disable()
            self.input6.Disable()
            self.text7.Disable()
            self.input7.Disable()
        
        
        

    
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=myframe()
    frame.Show()
    myapp.MainLoop()
