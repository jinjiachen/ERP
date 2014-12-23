#/usr/bin/env python
#coding=utf-8

import wx
import math

pi=3.14159265357

class PartsFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'零部件')
        panel=wx.Panel(self)
        type=['接管','支座','接头']
        wx.RadioBox(panel,-1,'请选择零部件',choices=type)
        
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=PartsFrame()
    frame.Show()
    myapp.MainLoop()
