# 画中国地区学员分布

import json
from pyecharts import options as opts
from pyecharts.charts import Geo

# city_one
file_path_one = r'D:\MaoDou\geoDataProject\ALL\city_data_one.json'
with open(file_path_one, 'r', encoding='utf-8') as f:
    city_data_one = json.load(f)

city_values_one = [(city['name'], city['value']) for city in city_data_one]

valid_city_values_one = []
for name, value in city_values_one:
        valid_city_values_one.append((name, value))

# city_two
file_path_two = r'D:\MaoDou\geoDataProject\ALL\city_data_two.json'
with open(file_path_two, 'r', encoding='utf-8') as f:
    city_data_two = json.load(f)

city_values_two = [(city['name'], city['value']) for city in city_data_two]

valid_city_values_two = []
for name, value in city_values_two:
        valid_city_values_two.append((name, value))

# city_three
file_path_three = r'D:\MaoDou\geoDataProject\ALL\city_data_three.json'
with open(file_path_three, 'r', encoding='utf-8') as f:
    city_data_three = json.load(f)

city_values_three = [(city['name'], city['value']) for city in city_data_three]

valid_city_values_three = []
for name, value in city_values_three:
        valid_city_values_three.append((name, value))

# city_four
file_path_four = r'D:\MaoDou\geoDataProject\ALL\city_data_four.json'
with open(file_path_four, 'r', encoding='utf-8') as f:
    city_data_four = json.load(f)

city_values_four = [(city['name'], city['value']) for city in city_data_four]

valid_city_values_four = []
for name, value in city_values_four:
        valid_city_values_four.append((name, value))

# city_five
file_path_five = r'D:\MaoDou\geoDataProject\ALL\city_data_five.json'
with open(file_path_five, 'r', encoding='utf-8') as f:
    city_data_five = json.load(f)

city_values_five = [(city['name'], city['value']) for city in city_data_five]

valid_city_values_five = []
for name, value in city_values_five:
        valid_city_values_five.append((name, value))

# city_six
file_path_six = r'D:\MaoDou\geoDataProject\ALL\city_data_six.json'
with open(file_path_six, 'r', encoding='utf-8') as f:
    city_data_six = json.load(f)

city_values_six = [(city['name'], city['value']) for city in city_data_six]

valid_city_values_six = []
for name, value in city_values_six:
        valid_city_values_six.append((name, value))

# province
file_province_path = r'D:\MaoDou\geoDataProject\ALL\province_data.json'
with open(file_province_path, 'r', encoding='utf-8') as f:
    province_data = json.load(f)

province_values = [(province['name'], province['value']) for province in province_data]

valid_province_values = []
for name, value in province_values:
    valid_province_values.append((name, value))


# 创建一个Geo地图
geo = Geo()

geo.add_schema(
    maptype="china",
    itemstyle_opts=opts.ItemStyleOpts(
        area_color="white",  # 设置地图的区域颜色为黄色
        border_color="orange",  # 设置边界的颜色
        border_width=0.5  # 设置边界宽度
    ),

)

# city one
geo.add(
    "训练营学员",
    valid_city_values_one,
    symbol_size=13,  # 根据学员数量调整点的大小
    color="red",
    itemstyle_opts=opts.ItemStyleOpts(
    color="red",  # 设置点的填充颜色为橙色
    border_color="red",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="red",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

# city 2
geo.add(
    "训练营学员",
    valid_city_values_two,
    symbol_size=11,  # 根据学员数量调整点的大小
    color="red",
    itemstyle_opts=opts.ItemStyleOpts(
    color="red",  # 设置点的填充颜色为橙色
    border_color="red",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="red",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

# city 3
geo.add(
    "训练营学员",
    valid_city_values_three,
    symbol_size=9,  # 根据学员数量调整点的大小
    color="red",
    itemstyle_opts=opts.ItemStyleOpts(
    color="red",  # 设置点的填充颜色为橙色
    border_color="red",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="red",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

# city 4
geo.add(
    "训练营学员",
    valid_city_values_four,
    symbol_size=8,  # 根据学员数量调整点的大小
    color="orangered",
    itemstyle_opts=opts.ItemStyleOpts(
    color="orangered",  # 设置点的填充颜色为橙色
    border_color="orangered",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="orangered",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

# city 5
geo.add(
    "训练营学员",
    valid_city_values_five,
    symbol_size=7,  # 根据学员数量调整点的大小
    color="orangered",
    itemstyle_opts=opts.ItemStyleOpts(
    color="orangered",  # 设置点的填充颜色为橙色
    border_color="orangered",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="orangered",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

# city 6
geo.add(
    "训练营学员",
    valid_city_values_six,
    symbol_size=5,  # 根据学员数量调整点的大小
    color="orange",
    itemstyle_opts=opts.ItemStyleOpts(
    color="orange",  # 设置点的填充颜色为橙色
    border_color="orange",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="red",
    ),
    label_opts=opts.LabelOpts(
        is_show=True,  # 显示标签
        position="top",  # 标签位置设置为点的上方
        formatter="{b}",  # 显示城市名称
        font_size=4,  # 标签字体大小
        color="black",  # 标签字体颜色
    )
)

geo.set_global_opts(
    title_opts=opts.TitleOpts(
        title="训练营平台用户地理位置分布图",
        title_textstyle_opts=opts.TextStyleOpts(
            color="red",  # 标题颜色
            font_size=20,  # 字体大小
            font_weight="bold",  # 字体粗细
            font_family="Arial",  # 字体类型
            # font_style="italic",  # 字体样式（斜体）
            border_color="darkred",  # 边框颜色
            border_width=10,
        )
    )
)

geo.render_notebook()
geo.render(r'D:\MaoDou\geoDataProject\ALL\china_city_map.html')
