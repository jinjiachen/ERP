#coding=cp936

import wx
import format


class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'��Ӷ������')
        panel=wx.Panel(self)
        list1=['���ְ�','Բ�ְ�','�ֹ�','Բ��','��ϼ�']
        list2=['Q245R','Q235B','20']
        list3=['��','�⹺','ZY','ZY,��ͼ','��ͼ','�⹺,��ͼ','���޸�']
        





if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=myframe()
    frame.Show()
    myapp.MainLoop()
