import xlrd
import numpy as np
file5="D:\\数学建模\\practice\\1_case_1_result-1.xls"
case_1_result=np.zeros([800,3])
data=xlrd.open_workbook(file5)
sheel=data.sheet_by_index(0)


for row in range(0,800):
    for col in range(sheel.ncols):
        case_1_result[row,col]=sheel.cell_value(row+1,col)


r=[1,2,3,4,5,6,7,8]
print(case_1_result)
# for row in 
# if case_1_result[0,]