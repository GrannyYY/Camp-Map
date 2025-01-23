# 画中国地区学员分布

import json
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# city_one
file_path_one = r'D:\MaoDou\geoDataProject\Rust\city_data_one.json'
with open(file_path_one, 'r', encoding='utf-8') as f:
    city_data_one = json.load(f)

city_values_one = [(city['name'], city['value']) for city in city_data_one]

valid_city_values_one = []
for name, value in city_values_one:
        valid_city_values_one.append((name, value))

# city_two
file_path_two = r'D:\MaoDou\geoDataProject\Rust\city_data_two.json'
with open(file_path_two, 'r', encoding='utf-8') as f:
    city_data_two = json.load(f)

city_values_two = [(city['name'], city['value']) for city in city_data_two]

valid_city_values_two = []
for name, value in city_values_two:
        valid_city_values_two.append((name, value))

# city_three
file_path_three = r'D:\MaoDou\geoDataProject\Rust\city_data_three.json'
with open(file_path_three, 'r', encoding='utf-8') as f:
    city_data_three = json.load(f)

city_values_three = [(city['name'], city['value']) for city in city_data_three]

valid_city_values_three = []
for name, value in city_values_three:
        valid_city_values_three.append((name, value))

# city_four
file_path_four = r'D:\MaoDou\geoDataProject\Rust\city_data_four.json'
with open(file_path_four, 'r', encoding='utf-8') as f:
    city_data_four = json.load(f)

city_values_four = [(city['name'], city['value']) for city in city_data_four]

valid_city_values_four = []
for name, value in city_values_four:
        valid_city_values_four.append((name, value))

# city_five
file_path_five = r'D:\MaoDou\geoDataProject\Rust\city_data_five.json'
with open(file_path_five, 'r', encoding='utf-8') as f:
    city_data_five = json.load(f)

city_values_five = [(city['name'], city['value']) for city in city_data_five]

valid_city_values_five = []
for name, value in city_values_five:
        valid_city_values_five.append((name, value))

# city_six
file_path_six = r'D:\MaoDou\geoDataProject\Rust\city_data_six.json'
with open(file_path_six, 'r', encoding='utf-8') as f:
    city_data_six = json.load(f)

city_values_six = [(city['name'], city['value']) for city in city_data_six]

valid_city_values_six = []
for name, value in city_values_six:
        valid_city_values_six.append((name, value))

# province
file_province_path = r'D:\MaoDou\geoDataProject\Rust\province_data.json'
with open(file_province_path, 'r', encoding='utf-8') as f:
    province_data = json.load(f)

province_values = [(province['name'], province['value']) for province in province_data]

valid_province_values = []
for name, value in province_values:
    valid_province_values.append((name, value))


# 海外
# #Rust
locations = [
    {"name": "spacemarket株式会社", "coords": [139.6917, 35.6895]},  # 东京，日本
    {"name": "INSA", "coords": [4.8282, 45.7821]},  # 里昂，法国
    {"name": "山东外国语职业技术大学", "coords": [119.4612, 36.7069]},  # 山东，中国
    {"name": "布朗大学", "coords": [-71.4025, 41.8268]},  # 罗德岛，美国
    {"name": "都柏林三一学院", "coords": [-6.2535, 53.3438]},  # 都柏林，爱尔兰
    {"name": "Eurecom", "coords": [7.0421, 43.6150]},  # 索菲亚安提波利斯，法国
    {"name": "西安电子科技大学", "coords": [108.9143, 34.2420]},  # 西安，中国
    {"name": "University of Tartu", "coords": [26.7150, 58.3780]},  # 塔尔图，爱沙尼亚
    {"name": "英国雷松（Raymarine）公司", "coords": [-1.1784, 50.9097]},  # 汉普郡，英国
    {"name": "卡尔斯鲁厄理工学院", "coords": [8.4146, 49.0134]},  # 卡尔斯鲁厄，德国
    {"name": "北亚利桑那大学", "coords": [-111.6549, 35.1852]},  # 弗拉格斯塔夫，美国
    {"name": "马里兰大学", "coords": [-76.9425, 38.9869]},  # 马里兰州，美国
    {"name": "Imperial College London", "coords": [-0.1764, 51.4988]},  # 伦敦，英国
    {"name": "慕尼黑大学", "coords": [11.5802, 48.1508]},  # 慕尼黑，德国
    {"name": "多伦多大学", "coords": [-79.3832, 43.6629]},  # 多伦多，加拿大
    {"name": "墨尔本大学", "coords": [144.9631, -37.7991]},  # 墨尔本，澳大利亚
    {"name": "politecnico di torino", "coords": [7.6593, 45.0646]},  # 都灵，意大利
    {"name": "悉尼大学", "coords": [151.1889, -33.8888]},  # 悉尼，澳大利亚
    {"name": "KTH Royal Institute of Technology", "coords": [18.0735, 59.3472]},  # 斯德哥尔摩，瑞典
    {"name": "京都大学", "coords": [135.7821, 35.0264]},  # 京都，日本
    {"name": "西九州大学", "coords": [130.2994, 33.2846]},  # 佐贺，日本
    {"name": "帝国理工学院", "coords": [-0.1764, 51.4988]},  # 伦敦，英国
]


# 创建一个Geo地图
geo = Geo()

geo.add_schema(
    maptype="world",
    itemstyle_opts=opts.ItemStyleOpts(
        area_color="white",  # 设置地图的区域颜色为黄色
        border_color="orange",  # 设置边界的颜色
        border_width=0.5  # 设置边界宽度
    ),
)

# 添加地点到地图
for location in locations:
    name = location["name"]
    coords = location["coords"]
    if coords != [0, 0]:  # 过滤未知地点
        geo.add_coordinate(name, coords[0], coords[1])  # 添加坐标
        geo.add(
            series_name="",
            data_pair=[(name, 1)],  # 数据对，值为1表示显示一个点
            symbol_size=3,  # 点的大小
            color="#14c077 ",  # 点的颜色
            # label_opts=opts.LabelOpts(
            #     is_show=True,
            #     formatter="{b}"
            # ),  # 显示标签
        )

# city one
geo.add(
    "训练营学员",
    valid_city_values_one,
    symbol_size=5,  # 根据学员数量调整点的大小d
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077 ",  # 设置点的填充颜色为橙色
    border_color="#14c077 ",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077 ",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

# city 2
geo.add(
    "训练营学员",
    valid_city_values_two,
    symbol_size=4,  # 根据学员数量调整点的大小
    color="#14c077 ",
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077 ",  # 设置点的填充颜色为橙色
    border_color="#14c077 ",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077 ",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

# city 3
geo.add(
    "训练营学员",
    valid_city_values_three,
    symbol_size=3,  # 根据学员数量调整点的大小
    color="#14c077 ",
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077 ",  # 设置点的填充颜色为橙色
    border_color="#14c077 ",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077 ",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

# city 4
geo.add(
    "训练营学员",
    valid_city_values_four,
    symbol_size=3,  # 根据学员数量调整点的大小
    color="#14c077",
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077",  # 设置点的填充颜色为橙色
    border_color="#14c077",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

# city 5
geo.add(
    "训练营学员",
    valid_city_values_five,
    symbol_size=2,  # 根据学员数量调整点的大小
    color="#14c077",
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077",  # 设置点的填充颜色为橙色
    border_color="#14c077",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

# city 6
geo.add(
    "训练营学员",
    valid_city_values_six,
    symbol_size=2,  # 根据学员数量调整点的大小
    color="#14c077",
    itemstyle_opts=opts.ItemStyleOpts(
    color="#14c077",  # 设置点的填充颜色为橙色
    border_color="#14c077",  # 设置边框颜色为红色
    border_width=0.3  # 设置边框宽度
    ),
    effect_opts=opts.EffectOpts(
        is_show=True,
        color="#14c077",
    ),
    # label_opts=opts.LabelOpts(
    #     is_show=True,  # 显示标签
    #     position="top",  # 标签位置设置为点的上方
    #     formatter="{b}",  # 显示城市名称
    #     font_size=4,  # 标签字体大小
    #     color="black",  # 标签字体颜色
    # )
)

geo.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Rust训练营学员地理位置分布图",
        subtitle="报名人数：1822 人\n来自高校：744 所\n来自城市：190 个",  # 添加副标题
        title_textstyle_opts=opts.TextStyleOpts(
            color="#14c077",  # 标题颜色
            font_size=20,  # 字体大小
            font_weight="bold",  # 字体粗细
            font_family="Arial",  # 字体类型
            # font_style="italic",  # 字体样式（斜体）
            border_color="darkred",  # 边框颜色
            border_width=10,
        ),
        subtitle_textstyle_opts=opts.TextStyleOpts(
            color="#78998b",  # 副标题颜色
            font_size=14,  # 副标题字体大小
            font_family="Arial",  # 字体类型
            font_weight="normal",  # 副标题字体粗细
        ),

    )
)

geo.render_notebook()

geo.render(r'D:\MaoDou\geoDataProject\Rust\Rust_world_map.html')
