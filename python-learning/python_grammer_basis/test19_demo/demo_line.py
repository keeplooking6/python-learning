from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,VisualMapOpts,TooltipOpts
line = Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,20,10])
line.set_global_opts(
    title_opts=TitleOpts(is_show=True,title="GDP",pos_left="center",pos_bottom="1%"),
    legend_opts = LegendOpts(is_show = True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
line.render()