#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook
import volume_calc

def exc(x1,m,x2,x3,x4,x5,x6):
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
    ws['E2']=u'单重'
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
    #第3行
    ws['A5']=3
    ws['B5']=u'接管'
    ws['C5']=x6
    ws['D5']=1
    ws['E5']='x'
    ws['F5']=ws['E5'].value*ws['D5'].value
    #第4行
    ws['A6']=4
    ws['B6']=x3
    ws['C6']='Q245B'
    ws['D6']=1
    ws['E6']='x'
    ws['F6']=ws['E6'].value*ws['D6'].value
    #第5行
    ws['A7']=5
    ws['B7']=x4
    ws['C7']='Q245B'
    ws['D7']=1
    ws['E7']='x'
    ws['F7']=ws['E7'].value*ws['D7'].value
    #第6行
    ws['A8']=6
    ws['B8']=x5
    ws['C8']='Q245B'
    ws['D8']=1
    ws['E8']='x'
    ws['F8']=ws['E8'].value*ws['D8'].value
    #test
#    for i in range(3,10):
#        ws.cell(row=i,column=1).value=i-2

    wb.save('D:\sample'+'s.xlsx')



