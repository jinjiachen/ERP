#coding=cp936
import wx

class MDIFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self,None,-1,'����ϵͳ')
        menu=wx.Menu()
        menu.Append(5000,'&�㲿��')
        menu.Append(5001,'&ѹ������')
        menu.Append(5002,'&������')
        menu.Append(6000,'&�˳�')
        menubar=wx.MenuBar()
        menubar.Append(menu,'&�ļ�')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.parts,id=5000)
        self.Bind(wx.EVT_MENU,self.volume,id=5001)
        self.Bind(wx.EVT_MENU,self.volume,id=5002)
        self.Bind(wx.EVT_MENU,self.OnExit,id=6000)

    def OnExit(self,event):
        self.Close(True)

    def parts(self,event):
        win=wx.MDIChildFrame(self,-1,'�㲿��')
        #panel=wx.Panel(self)
        wx.StaticText(self,-1,'����',(50,50))
        win.Show(True)

    def volume(self,event):
        win=wx.MDIChildFrame(self,-1,'ѹ������')
        win.Show(True)

    def volume(self,event):
        win=wx.MDIChildFrame(self,-1,'������')
        win.Show(True)


if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=MDIFrame()
    myframe.Show()
    myapp.MainLoop()
