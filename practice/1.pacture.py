import xlrd
import numpy as np
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
from matplotlib.font_manager import FontProperties
font_set= FontProperties(fname=r"C:\\windows\\fonts\\simsun.ttc",size=12)
file5="D:\\数学建模\\practice\\1_case_1_result-1.xls"
case_1_result=np.zeros([800,3])
data=xlrd.open_workbook(file5)
sheel=data.sheet_by_index(0)

nmax=[0,0,0,0,0,0,0,0]
for row in range(0,800):
    for col in range(sheel.ncols):
        case_1_result[row,col]=sheel.cell_value(row+1,col)


r=[1,2,3,4,5,6,7,8]
# print(case_1_result)
for j in range(0,8):
    max=-1
    for row in range(0,800):
        if case_1_result[row,0]==j:
            if case_1_result[row,1]>=max:
                max=case_1_result[row,1]
                nmax[j]=max
fig=plt.figure()

plt.plot(r,nmax, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='一些数字')
for a, b in zip(r, nmax):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    #第二个b代表加的是y轴的数据  ，这里的a,b是坐标轴
plt.xlabel(u"cnc编号",fontproperties=font_set)
plt.ylabel(u"结束时间",fontproperties=font_set)
plt.title(u"时间表",fontproperties=font_set)
plt.savefig('时间折线图.png')
plt.show()  
