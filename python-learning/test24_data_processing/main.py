# 计算这两个月每一天的销售额
from pyecharts.globals import ThemeType

from data_define import Record
from file_define import TextFileReader,JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts,LabelOpts,InitOpts

textfile = TextFileReader("2011年1月销售数据.txt")
jsonfile = JsonFileReader("2011年2月销售数据JSON.txt")

text_record_list: list[Record] = textfile.read_file()
json_record_list: list[Record] = jsonfile.read_file()
# for l in text_record_list:
#     print(l.money)
all_record: list[Record] = text_record_list + json_record_list
# for l in all_record:
#     print(l)
dict_sale = {}
for x in all_record:
    if x.date in dict_sale.keys():
        dict_sale[x.date] += int(x.money)
        # print(type(dict_sale[x.date]))
    else:
        dict_sale[x.date] = int(x.money)

        # print(type(dict_sale[x.date]))
print(dict_sale)

bar = Bar(init_opts=InitOpts(theme = ThemeType.LIGHT))
bar.add_xaxis(list(dict_sale.keys())) # 需要的参数是list类型
bar.add_yaxis("销售额",list(dict_sale.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title = "每日销售额")

)
bar.render("data.html")
