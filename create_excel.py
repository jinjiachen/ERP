#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook
import volume_calc

def exc(x1,m,x2,x3,x4,x5,x6):
    wb=Workbook()
    ws=wb.active
    ws.title=u'���۵�'
#����
    ws.merge_cells('A1:F1')
    ws['A1']=u'ѹ���������۱�'
    ws['A2']=u'���'
    ws['B2']=u'����'
    ws['C2']=u'����'
    ws['D2']=u'����'
    ws['E2']=u'����'
    ws['F2']=u'����'
#���п�ʼд������
    #��1��
    ws['A3']=1
    ws['B3']=u'Ͳ��'
    ws['C3']=x1
    ws['D3']=1
    ws['E3']=m
    ws['F3']=ws['E3'].value*ws['D3'].value
    #��2��
    ws['A4']=2
    ws['B4']=u'��ͷ'
    ws['C4']='Q245R'
    ws['D4']=2
    ws['E4']=x2
    ws['F4']=ws['E4'].value*ws['D4'].value
    #��3��
    ws['A5']=3
    ws['B5']=u'�ӹ�'
    ws['C5']=x6
    ws['D5']=1
    ws['E5']='x'
    ws['F5']=ws['E5'].value*ws['D5'].value
    #��4��
    ws['A6']=4
    ws['B6']=x3
    ws['C6']='Q245B'
    ws['D6']=1
    ws['E6']='x'
    ws['F6']=ws['E6'].value*ws['D6'].value
    #��5��
    ws['A7']=5
    ws['B7']=x4
    ws['C7']='Q245B'
    ws['D7']=1
    ws['E7']='x'
    ws['F7']=ws['E7'].value*ws['D7'].value
    #��6��
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



