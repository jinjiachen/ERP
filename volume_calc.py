#/usr/bin/env python
#coding=utf-8

import wx
import math

pi=3.14159265357

class VolumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'ѹ������')
        self.panel=wx.Panel(self)
        type=['��֪����','δ֪����']
        self.singlebox=wx.RadioBox(self.panel,-1,'��ѡ������',choices=type)
        #������ʼ����
        self.text1=wx.StaticText(self.panel,-1,'���ѹ��(MPa)',(20,80))
        self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
        self.text2=wx.StaticText(self.panel,-1,'����ϵ��',(20,120))
        self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
        self.text3=wx.StaticText(self.panel,-1,'ѡ��Ӧ��(MPa)',(20,160))
        self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
        self.text4=wx.StaticText(self.panel,-1,'�������ݻ�(m^3)',(20,200))
        self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
        self.text5=wx.StaticText(self.panel,-1,'Ͳ��ĳ���(mm)',(20,240))
        self.input5=wx.TextCtrl(self.panel,-1,'',(120,240))
        self.text6=wx.StaticText(self.panel,-1,'Ͳ��ıں�(mm)',(20,280))
        self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
        self.text7=wx.StaticText(self.panel,-1,'Ͳ���ֱ��(mm)',(20,320))
        self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
        self.text8=wx.StaticText(self.panel,-1,'��ͷ�ߴ�(mm)',(20,360))
        self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
        self.text9=wx.StaticText(self.panel,-1,'��ͷ�ں�(mm)',(20,400))
        self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))


        self.Bind(wx.EVT_RADIOBOX,self.GetIndex,self.singlebox)

    def GetIndex(self,event):
        if self.singlebox.GetSelection()==0:#��ͬ��ѡ���Ӧ��ͬ�Ĳ���
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

            self.text1=wx.StaticText(self.panel,-1,'���ѹ��(MPa)',(20,80))
            self.input1=wx.TextCtrl(self.panel,-1,'',(120,80))
            self.text2=wx.StaticText(self.panel,-1,'����ϵ��',(20,120))
            self.input2=wx.TextCtrl(self.panel,-1,'',(120,120))
            self.text3=wx.StaticText(self.panel,-1,'ѡ��Ӧ��(MPa)',(20,160))
            self.input3=wx.TextCtrl(self.panel,-1,'',(120,160))
            self.text4=wx.StaticText(self.panel,-1,'�������ݻ�(m^3)',(20,200))
            self.input4=wx.TextCtrl(self.panel,-1,'',(120,200))
            self.text5=wx.StaticText(self.panel,-1,'Ͳ��ĳ���(mm)',(20,240))
            self.input5=wx.TextCtrl(self.panel,-1,'',(120,240))
            self.text6=wx.StaticText(self.panel,-1,'Ͳ��ıں�(mm)',(20,280))
            self.input6=wx.TextCtrl(self.panel,-1,'',(120,280))
            self.text7=wx.StaticText(self.panel,-1,'Ͳ���ֱ��(mm)',(20,320))
            self.input7=wx.TextCtrl(self.panel,-1,'',(120,320))
            self.text8=wx.StaticText(self.panel,-1,'��ͷ�ߴ�(mm)',(20,360))
            self.input8=wx.TextCtrl(self.panel,-1,'',(120,360))
            self.text9=wx.StaticText(self.panel,-1,'��ͷ�ں�(mm)',(20,400))
            self.input9=wx.TextCtrl(self.panel,-1,'',(120,400))
            


#            text1=wx.StaticText(self.panel,-1,'�������ݻ�(m^3)',(20,80))
#            wx.TextCtrl(self.panel,-1,'',(120,80))
#            text2=wx.StaticText(self.panel,-1,'Ͳ��ĳ���(mm)',(20,120))
#            wx.TextCtrl(self.panel,-1,'',(120,120))
#            text3=wx.StaticText(self.panel,-1,'Ͳ��ıں�(mm)',(20,160))
#            wx.TextCtrl(self.panel,-1,'',(120,160))
#            text4=wx.StaticText(self.panel,-1,'Ͳ���ֱ��(mm)',(20,200))
#            wx.TextCtrl(self.panel,-1,'',(120,200))
#            text5=wx.StaticText(self.panel,-1,'��ͷ�ߴ�(mm)',(20,240))
#            wx.TextCtrl(self.panel,-1,'',(120,240))
#            text6=wx.StaticText(self.panel,-1,'��ͷ�ں�(mm)',(20,280))
#            wx.TextCtrl(self.panel,-1,'',(120,280))
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
            
            self.text4.SetLabel('Ͳ��ĳ���(mm)')
            self.text5.SetLabel('Ͳ���ֱ��(mm)')
            self.text6.SetLabel('Ͳ��ıں�(mm)')
            self.text7.SetLabel('��ͷ�ĳߴ�(mm)')
            self.text8.SetLabel('��ͷ�ں�(mm)')
            self.text9.SetLabel('�������ݻ�(m^3)')
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=VolumeFrame()
    frame.Show()
    myapp.MainLoop()
