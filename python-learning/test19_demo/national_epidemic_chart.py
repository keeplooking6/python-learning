#
import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts,TitleOpts
American_file = open("美国.txt",'r',encoding="UTF-8")
Janpanese_file = open("日本.txt",'r',encoding="UTF-8")
India_file = open("印度.txt",'r',encoding="UTF-8")
# 去头
us_data = American_file.read().replace("jsonp_1629344292311_69436(", "")
jp_data = Janpanese_file.read().replace("jsonp_1629350871167_29498(","")
in_data = India_file.read().replace("jsonp_1629350745930_63180(","")
# 去尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 将json转为python数据
us_data = json.loads(us_data)
jp_data = json.loads(jp_data)
in_data = json.loads(in_data)
# 获取trend数据
us_trend_data = us_data['data'][0]['trend']
jp_trend_data = jp_data['data'][0]['trend']
in_trend_data = in_data['data'][0]['trend']
# 获取存放日期的数据，x轴(到下标314结束）
x_data = us_trend_data['updateDate'][:314]
# 获取存放人数的数据，y轴（到下标315结束）
us_y_data = us_trend_data['list'][0]['data']
jp_y_data = jp_trend_data['list'][0]['data']
in_y_data = in_trend_data['list'][0]['data']
line = Line()
line.add_xaxis(x_data)
# 将y轴的数字去掉
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="美日印三国的确诊人数分布")
)
line.render("epidemicCharts.html")
American_file.close()
Janpanese_file.close()
India_file.close()

