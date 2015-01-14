#coding=cp936
from openpyxl import Workbook
from openpyxl import load_workbook
import volume_calc

def exc(x1,cho1,cho2,m,x2,x6,length1,width1,height1,length2,width2,height2,length3,width3,height3,length4,width4,height4):
    wb=load_workbook('D:\sample.xlsx')
    ws=wb.active
    ws.title=u'报价单'
#搭框架
    ws.merge_cells('A1:F1')
    ws.cell(row=1,column=1).value=u'压力容器报价表'
    ws.cell(row=2,column=1).value=u'序号'
    ws.cell(row=2,column=2).value=u'名称'
    ws.cell(row=2,column=3).value=u'材料'
    ws.cell(row=2,column=4).value=u'数量'
    ws.cell(row=2,column=5).value=u'单重'
    ws.cell(row=2,column=6).value=u'总重'
#按行开始写入内容
    #筒体
    ws.cell(row=3,column=1).value=1
    ws.cell(row=3,column=2).value=u'筒体'
    ws.cell(row=3,column=3).value=x1
    ws.cell(row=3,column=4).value=1
    ws.cell(row=3,column=5).value=m
    ws.cell(row=3,column=6).value=ws.cell(row=3,column=5).value*ws.cell(row=3,column=4).value
    #封头
    ws.cell(row=4,column=1).value=2
    ws.cell(row=4,column=2).value=u'封头'
    ws.cell(row=4,column=3).value='Q245R'
    ws.cell(row=4,column=4).value=2
    ws.cell(row=4,column=5).value=x2
    ws.cell(row=4,column=6).value=ws.cell(row=4,column=5).value*ws.cell(row=4,column=4).value
    #接管
    if cho1.encode('cp936')<>'无':
        i=6
        ws.cell(row=5,column=1).value=3
        ws.cell(row=5,column=2).value=u'接管'
        ws.cell(row=5,column=3).value=x6
        ws.cell(row=5,column=4).value=1
        ws.cell(row=5,column=5).value=u'待填'
        ws.cell(row=5,column=6).value=ws.cell(row=5,column=5).value*ws.cell(row=5,column=4).value
    else:
        i=5

    if cho2==1:
    #腹板
        ws.cell(row=i,column=1).value=i-2
        ws.cell(row=i,column=2).value=u'腹板'
        ws.cell(row=i,column=3).value='Q245B'
        ws.cell(row=i,column=4).value=1
        ws.cell(row=i,column=5).value=plate(length1,width1,height1)
        ws.cell(row=i,column=6).value=ws.cell(row=i,column=5).value*ws.cell(row=i,column=4).value
    #筋板
        ws.cell(row=i+1,column=1).value=i-1
        ws.cell(row=i+1,column=2).value=u'筋板'
        ws.cell(row=i+1,column=3).value='Q245B'
        ws.cell(row=i+1,column=4).value=1
        ws.cell(row=i+1,column=5).value=plate(length2,width2,height2)
        ws.cell(row=i+1,column=6).value=ws.cell(row=i+1,column=5).value*ws.cell(row=i+1,column=4).value
    #底板
        ws.cell(row=i+2,column=1).value=i
        ws.cell(row=i+2,column=2).value=u'底板'
        ws.cell(row=i+2,column=3).value='Q245B'
        ws.cell(row=i+2,column=4).value=1
        ws.cell(row=i+2,column=5).value=plate(length3,width3,height3)
        ws.cell(row=i+2,column=6).value=ws.cell(row=i+2,column=5).value*ws.cell(row=i+2,column=4).value
    #垫板
        ws.cell(row=i+3,column=1).value=i+1
        ws.cell(row=i+3,column=2).value=u'垫板'
        ws.cell(row=i+3,column=3).value='Q245B'
        ws.cell(row=i+3,column=4).value=1
        ws.cell(row=i+3,column=5).value=plate(length4,width4,height4)
        ws.cell(row=i+3,column=6).value=ws.cell(row=i+3,column=5).value*ws.cell(row=i+3,column=4).value
    elif cho2==2:
        #腹板
        ws.cell(row=i,column=1).value=4
        ws.cell(row=i,column=2).value=u'腹板'
        ws.cell(row=i,column=3).value='Q245B'
        ws.cell(row=i,column=4).value=1
        ws.cell(row=i,column=5).value=plate(length1,width1,height1)
        ws.cell(row=i,column=6).value=ws.cell(row=i,column=5).value*ws.cell(row=i,column=4).value
    #筋板
        ws.cell(row=i+1,column=1).value=5
        ws.cell(row=i+1,column=2).value=u'筋板'
        ws.cell(row=i+1,column=3).value='Q245B'
        ws.cell(row=i+1,column=4).value=1
        ws.cell(row=i+1,column=5).value=plate(length2,width2,height2)
        ws.cell(row=i+1,column=6).value=ws.cell(row=i+1,column=5).value*ws.cell(row=i+1,column=4).value
    #底板
        ws.cell(row=i+2,column=1).value=6
        ws.cell(row=i+2,column=2).value=u'底板'
        ws.cell(row=i+2,column=3).value='Q245B'
        ws.cell(row=i+2,column=4).value=1
        ws.cell(row=i+2,column=5).value=plate(length3,width3,height3)
        ws.cell(row=i+2,column=6).value=ws.cell(row=i+2,column=5).value*ws.cell(row=i+2,column=4).value
    

    wb.save('D:\output.xlsx')


def plate(L,W,H):#计算平板
    L=float(L)
    W=float(W)
    H=float(H)
    m=L*W*H/1000**3*7850
    return(m)



