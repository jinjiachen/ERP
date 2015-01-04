#-*-coding:cp936-*-
#/usr/bin/python2.7

import wx
import math
import parts_calc
import volume_calc
import heat_transfer

pi=3.14159265357

class mainframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'����ϵͳ')
        menu=wx.Menu()
        menu.Append(5000,'&�㲿��')
        menu.Append(5001,'&ѹ������')
        menu.Append(5002,'&������')
        menu.Append(6000,'&�˳�')
        menubar=wx.MenuBar()
        menubar.Append(menu,'�ļ�')
        self.SetMenuBar(menubar)#����Ϊ�˵����Ĵ���

        panel=wx.Panel(self)

        #�����¼�
        self.Bind(wx.EVT_MENU,self.Onparts,id=5000)
        self.Bind(wx.EVT_MENU,self.Onvolume,id=5001)
        self.Bind(wx.EVT_MENU,self.Onheat,id=5002)
        self.Bind(wx.EVT_MENU,self.Exit,id=6000)

    #��������
    def Onparts(self,event):
        parts_calc.PartsFrame().Show()

    def Onvolume(self,event):
        volume_calc.VolumeFrame().Show()

    def Onheat(self,event):
        heat_transfer.HeatTransferFrame().Show()

    def Exit(self,event):
        self.Close(True)
    



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=mainframe()
    frame.Show()
    myapp.MainLoop()
