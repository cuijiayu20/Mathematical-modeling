import numpy
import pandas
from spsspro.algorithm import supervised_learning
import xlrd

file2="原始数据处理.xls"
data=xlrd.open_workbook(file2)
st=data.sheet_by_index(0)

#生成案例数据
data_x = pandas.DataFrame({
    
    "二氧化硅":[st.cell_value(i, 6) for i in range(1, 45)],
    "氧化钠":[st.cell_value(i, 7) for i in range(1, 45)],
    "氧化钾":[st.cell_value(i, 8) for i in range(1, 45)],
    "氧化钙":[st.cell_value(i, 9) for i in range(1, 45)],
    "氧化镁":[st.cell_value(i, 10) for i in range(1, 45)],
    "氧化铝":[st.cell_value(i, 11) for i in range(1, 45)],
    "氧化铁":[st.cell_value(i, 12) for i in range(1, 45)],
    "氧化铜":[st.cell_value(i, 13) for i in range(1, 45)],
    "氧化铅":[st.cell_value(i, 14) for i in range(1, 45)],
    "氧化钡":[st.cell_value(i, 15) for i in range(1, 45)],
    "五氧化二磷":[st.cell_value(i, 16) for i in range(1, 45)],
    "氧化锶":[st.cell_value(i, 17) for i in range(1, 45)],
    "氧化锡":[st.cell_value(i, 18) for i in range(1, 45)],
    "二氧化硫":[st.cell_value(i, 19) for i in range(1, 45)]
})
data_y = pandas.Series(data=numpy.random.choice([1, 2], size= 44), name="C")
#随机森林分类，
result = supervised_learning.random_forest_classifier(data_x=data_x, data_y=data_y)
print(result) 