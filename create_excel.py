#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook
import volume_calc

def exc(x1,m,x2):
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

    wb.save('D:\sample.xlsx')



