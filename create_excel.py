#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook

wb=Workbook()
ws=wb.active
ws.title='报价单'
ws['A2']='名称'
ws['B2']='材料'
ws['C2']='数量'
ws['D2']='重量'

wb.save('D:\sample.xlsx')



