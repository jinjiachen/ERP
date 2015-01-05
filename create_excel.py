#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook
import volume_calc

def exc(x1,m,x2):
    wb=Workbook()
    ws=wb.active
    ws.title=u'报价单'
#搭框架
    ws.merge_cells('A1:F1')
    ws['A1']=u'压力容器报价表'
    ws['A2']=u'序号'
    ws['B2']=u'名称'
    ws['C2']=u'材料'
    ws['D2']=u'数量'
    ws['E2']=u'单量'
    ws['F2']=u'总重'
#按行开始写入内容
    #第1行
    ws['A3']=1
    ws['B3']=u'筒体'
    ws['C3']=x1
    ws['D3']=1
    ws['E3']=m
    ws['F3']=ws['E3'].value*ws['D3'].value
    #第2行
    ws['A4']=2
    ws['B4']=u'封头'
    ws['C4']='Q245R'
    ws['D4']=2
    ws['E4']=x2
    ws['F4']=ws['E4'].value*ws['D4'].value

    wb.save('D:\sample.xlsx')



