#/usr/bin/env python
#coding=utf-8

import wx
import math

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

        self.Bind(wx.EVT_MENU,self.Exit,id=6000)

    def Exit(self,event):
        self.Close(True)
    



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=mainframe()
    frame.Show()
    myapp.MainLoop()
