#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook

wb=Workbook()
ws=wb.active
ws.title='���۵�'
ws['A2']='����'
ws['B2']='����'
ws['C2']='����'
ws['D2']='����'

wb.save('D:\sample.xlsx')



