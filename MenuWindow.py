#/usr/bin/python2.7
#coding:cp936

import wx
import math
import parts_calc
import volume_calc
import heat_transfer

pi=3.14159265357

class mainframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'报价系统')
        menu=wx.Menu()
        menu.Append(5000,'&零部件')
        menu.Append(5001,'&压力容器')
        menu.Append(5002,'&换热器')
        menu.Append(6000,'&退出')
        menubar=wx.MenuBar()
        menubar.Append(menu,'文件')
        self.SetMenuBar(menubar)#以上为菜单栏的创建

        panel=wx.Panel(self)

        #驱动事件
        self.Bind(wx.EVT_MENU,self.Onparts,id=5000)
        self.Bind(wx.EVT_MENU,self.Onvolume,id=5001)
        self.Bind(wx.EVT_MENU,self.Onheat,id=5002)
        self.Bind(wx.EVT_MENU,self.Exit,id=6000)

    #函数部分
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
