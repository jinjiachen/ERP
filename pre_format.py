#coding=cp936
import wx
import format

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'���϶���������')
        panel=wx.Panel(self)
        list1=['�ְ�','�ֹ�','Բ��']
        list2=['Q245R','Q235B','20']
        wx.StaticText(panel,-1,'ͼ��',(60,50))
        self.text1=wx.TextCtrl(panel,-1,'',(110,50))
        wx.StaticText(panel,-1,'����',(60,90))
        self.text2=wx.TextCtrl(panel,-1,'',(110,90))
        wx.StaticText(panel,-1,'����',(60,130))
        self.text3=wx.Choice(panel,-1,(110,130),choices=list1)
        wx.StaticText(panel,-1,'�ƺ�',(60,170))
        self.text4=wx.Choice(panel,-1,(110,170),choices=list2)
        wx.StaticText(panel,-1,'����',(60,210))
        self.text5=wx.TextCtrl(panel,-1,'',(110,210))
        wx.StaticText(panel,-1,'���',(60,250))
        self.text6=wx.TextCtrl(panel,-1,'',(110,250))
        wx.StaticText(panel,-1,'���',(60,290))
        self.text7=wx.TextCtrl(panel,-1,'',(110,290))
        wx.StaticText(panel,-1,'����',(60,330))
        self.text8=wx.TextCtrl(panel,-1,'',(110,330))
        button=wx.Button(panel,-1,'���',(110,370))
        self.Bind(wx.EVT_BUTTON,self.output,button)


        

    def output(self,event):
        x1=self.text1.GetValue()
        x2=self.text2.GetValue()
        x3=self.text3.GetStringSelection()
        x4=self.text4.GetStringSelection()
        x5=self.text5.GetValue()
        x6=self.text6.GetValue()
        x7=self.text7.GetValue()
        i=self.text8.GetValue()
        format.exc(x1,x2,x3,x4,x5,x6,x7,i)
        
        
        
        
        



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=Frame()
    myframe.Show()
    myapp.MainLoop()
