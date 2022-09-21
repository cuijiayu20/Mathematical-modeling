#聚类模型

import xlrd
import numpy
import pandas
from spsspro.algorithm import statistical_model_analysis
file1="数据处理2.xls"
data=xlrd.open_workbook(file1)
st=data.sheet_by_index(0)




#生成案例数据

data_x = pandas.DataFrame({
    "类型":[st.cell_value(i, 1) for i in range(1, 45)],
    "二氧化硅":[st.cell_value(i, 5) for i in range(1, 45)],
    "氧化钠":[st.cell_value(i, 6) for i in range(1, 45)],
    "氧化钾":[st.cell_value(i, 7) for i in range(1, 45)],
    "氧化钙":[st.cell_value(i, 8) for i in range(1, 45)],
    "氧化镁":[st.cell_value(i, 9) for i in range(1, 45)],
    "氧化铝":[st.cell_value(i, 10) for i in range(1, 45)],
    "氧化铁":[st.cell_value(i, 11) for i in range(1, 45)],
    "氧化铜":[st.cell_value(i, 12) for i in range(1, 45)],
    "氧化铅":[st.cell_value(i, 13) for i in range(1, 45)],
    "氧化钡":[st.cell_value(i, 14) for i in range(1, 45)],
    "五氧化二磷":[st.cell_value(i, 15) for i in range(1, 45)],
    "氧化锶":[st.cell_value(i, 16) for i in range(1, 45)],
    "氧化锡":[st.cell_value(i, 17) for i in range(1, 45)],
    "二氧化硫":[st.cell_value(i, 18) for i in range(1, 45)]
})
#聚类分析，输入参数详细可以光标放置函数括号内按shift+tab查看，输出结果参考spsspro模板分析报告
result = statistical_model_analysis.cluster_analysis(data, cluster_num=3)
print(result)