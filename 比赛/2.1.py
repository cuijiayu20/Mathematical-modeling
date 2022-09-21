#随机打乱程序
import random
import xlrd
import xlwt
file1="D:\数学建模\比赛\数据处理2.xls"
data=xlrd.open_workbook(file1)
lis1=[]
sheet= data.sheet_by_index(0)
lis=random.sample(range(1,sheet.nrows), sheet.nrows-1)
lis1.append([sheet.cell_value(0,j) for j in range(0,sheet.ncols)])
for i in lis:
    
    lis1.append([sheet.cell_value(i,j) for j in range(0,sheet.ncols)])


book=xlwt.Workbook()
sheet1= book.add_sheet("sheet1",cell_overwrite_ok=True)
for row in range(len(lis1)):
    for col in range(len(lis1[0])):
        sheet1.write(row,col,lis1[row][col])

book.save("数据处理3.xls")
