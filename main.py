#coding=cp936
import wx

class MDIFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self,None,-1,'报价系统')
        menu=wx.Menu()
        menu.Append(5000,'&零部件')
        menu.Append(5001,'&压力容器')
        menu.Append(5002,'&换热器')
        menu.Append(6000,'&退出')
        menubar=wx.MenuBar()
        menubar.Append(menu,'&文件')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.parts,id=5000)
        self.Bind(wx.EVT_MENU,self.volume,id=5001)
        self.Bind(wx.EVT_MENU,self.volume,id=5002)
        self.Bind(wx.EVT_MENU,self.OnExit,id=6000)

    def OnExit(self,event):
        self.Close(True)

    def parts(self,event):
        win=wx.MDIChildFrame(self,-1,'零部件')
        #panel=wx.Panel(self)
        wx.StaticText(self,-1,'试试',(50,50))
        win.Show(True)

    def volume(self,event):
        win=wx.MDIChildFrame(self,-1,'压力容器')
        win.Show(True)

    def volume(self,event):
        win=wx.MDIChildFrame(self,-1,'换热器')
        win.Show(True)


if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=MDIFrame()
    myframe.Show()
    myapp.MainLoop()
