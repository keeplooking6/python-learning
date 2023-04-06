from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ('北京市',99),
    ('上海市',590),
    ('广东省',299),
    ('云南省',1009)
]
map.add("test",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":200,"label":"1-200人","color":"grey"},
            {"min":201,"max":500,"label":"201-500人","color":"blue"},
            {"min":501,"max":1000,"label":"501-1000人","color":"orange"},
            {"min":1000,"label":"1000人以上","color":"red"},
        ]
    )
)
map.render("demo_map.html")