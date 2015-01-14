#coding=cp936

import wx
import format


class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'添加额外零件')
        panel=wx.Panel(self)
        list1=['方钢板','圆钢板','钢管','圆钢','组合件']
        list2=['Q245R','Q235B','20']
        list3=['无','外购','ZY','ZY,无图','无图','外购,无图','需修改']
        





if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=myframe()
    frame.Show()
    myapp.MainLoop()
