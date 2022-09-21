#用与处理数据
import xlrd
import xlwt
file="D:\数学建模\比赛\附件(数据排序xls).xls"
data=xlrd.open_workbook(file)
sheet=data.sheet_by_index(0)
sheet1=data.sheet_by_index(1)
lis1=[]
lis2=[]

lis4=[]
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        lis1.append(sheet.cell_value(row,col))

for row in range(sheet1.nrows):
    for col in range(sheet1.ncols):
        lis2.append(sheet1.cell_value(row,col))
for row in range(1,sheet.nrows):
    for row1 in range(1,sheet1.nrows):
        lis3=[]
        if sheet.cell_value(row,0)==sheet1.cell_value(row1,0):
            for col in range(sheet.ncols):
                lis3.append(sheet.cell_value(row,col))
            for col1 in range(sheet1.ncols):
                lis3.append(sheet1.cell_value(row1,col1))
            lis4.append(lis3)
book=xlwt.Workbook()
sheet= book.add_sheet("sheet1",cell_overwrite_ok=True)
for row in range(len(lis4)):
    for col in range(len(lis4[0])):
        sheet.write(row,col,lis4[row][col])
       

book.save("数据处理.xls")

#调用相关性模型
import pandas
import xlrd
from spsspro.algorithm import descriptive_analysis
file1="sperman_4.xls"
data=xlrd.open_workbook(file1)
st=data.sheet_by_index(0)


data = pandas.DataFrame({
    "纹饰":[st.cell_value(i, 1) for i in range(1, st.nrows)],
    "类型1":[st.cell_value(i, 2) for i in range(1, st.nrows)],
    "类型2":[st.cell_value(i, 3) for i in range(1, st.nrows)],
    "深绿":[st.cell_value(i, 4) for i in range(1, st.nrows)],
    "深蓝":[st.cell_value(i, 5) for i in range(1, st.nrows)],
    "浅蓝":[st.cell_value(i, 6) for i in range(1, st.nrows)],
    "蓝绿":[st.cell_value(i, 7) for i in range(1, st.nrows)],
    "紫":[st.cell_value(i, 8) for i in range(1, st.nrows)],
    "浅绿":[st.cell_value(i, 9) for i in range(1, st.nrows)],
    "深绿":[st.cell_value(i, 10) for i in range(1, st.nrows)],
    "绿":[st.cell_value(i, 11) for i in range(1, st.nrows)],
    "表面":[st.cell_value(i, 12) for i in range(1, st.nrows)],
    "二氧化硅":[st.cell_value(i, 13) for i in range(1, st.nrows)],
    "氧化钠":[st.cell_value(i, 14) for i in range(1, st.nrows)],
    "氧化钾":[st.cell_value(i, 15) for i in range(1, st.nrows)],
    "氧化钙":[st.cell_value(i, 16) for i in range(1, st.nrows)],
    "氧化镁":[st.cell_value(i, 17) for i in range(1, st.nrows)],
    "氧化铝":[st.cell_value(i, 18) for i in range(1, st.nrows)],
    "氧化铁":[st.cell_value(i, 19) for i in range(1,st.nrows)],
    "氧化铜":[st.cell_value(i, 20) for i in range(1, st.nrows)],
    "氧化铅":[st.cell_value(i, 21) for i in range(1, st.nrows)],
    "氧化钡":[st.cell_value(i, 22) for i in range(1, st.nrows)],
    "五氧化二磷":[st.cell_value(i, 23) for i in range(1, st.nrows)],
    "氧化锶":[st.cell_value(i, 24) for i in range(1, st.nrows)],
    "氧化锡":[st.cell_value(i, 25) for i in range(1, st.nrows)],
    "二氧化硫":[st.cell_value(i, 26) for i in range(1, st.nrows)]
})
#相关性分析，输入参数详细可以光标放置函数括号内按shift+tab查看，输出结果参考spsspro模板分析报告
result = descriptive_analysis.correlation_analysis(data)
print(result)
