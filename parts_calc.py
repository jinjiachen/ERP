#/usr/bin/env python
#coding=utf-8

import wx
import math

pi=3.14159265357

class PartsFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'�㲿��')
        panel=wx.Panel(self)
        type=['�ӹ�','֧��','��ͷ']
        wx.RadioBox(panel,-1,'��ѡ���㲿��',choices=type)
        
            
            



if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=PartsFrame()
    frame.Show()
    myapp.MainLoop()
