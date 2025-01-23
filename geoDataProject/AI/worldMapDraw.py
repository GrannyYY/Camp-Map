# 画中国地区学员分布

import json
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# city_one
file_path_one = r'D:\MaoDou\geoDataProject\AI\city_data_one.json'
with open(file_path_one, 'r', encoding='utf-8') as f:
    city_data_one = json.load(f)

city_values_one = [(city['name'], city['value']) for city in city_data_one]

valid_city_values_one = []
for name, value in city_values_one:
        valid_city_values_one.append((name, value))

# city_two
file_path_two = r'D:\MaoDou\geoDataProject\AI\city_data_two.json'
with open(file_path_two, 'r', encoding='utf-8') as f:
    city_data_two = json.load(f)

city_values_two = [(city['name'], city['value']) for city in city_data_two]

valid_city_values_two = []
for name, value in city_values_two:
        valid_city_values_two.append((name, value))

# city_three
file_path_three = r'D:\MaoDou\geoDataProject\AI\city_data_three.json'
with open(file_path_three, 'r', encoding='utf-8') as f:
    city_data_three = json.load(f)

city_values_three = [(city['name'], city['value']) for city in city_data_three]

valid_city_values_three = []
for name, value in city_values_three:
        valid_city_values_three.append((name, value))

# city_four
file_path_four = r'D:\MaoDou\geoDataProject\AI\city_data_four.json'
with open(file_path_four, 'r', encoding='utf-8') as f:
    city_data_four = json.load(f)

city_values_four = [(city['name'], city['value']) for city in city_data_four]

valid_city_values_four = []
for name, value in city_values_four:
        valid_city_values_four.append((name, value))

# city_five
file_path_five = r'D:\MaoDou\geoDataProject\AI\city_data_five.json'
with open(file_path_five, 'r', encoding='utf-8') as f:
    city_data_five = json.load(f)

city_values_five = [(city['name'], city['value']) for city in city_data_five]

valid_city_values_five = []
for name, value in city_values_five:
        valid_city_values_five.append((name, value))

# city_six
file_path_six = r'D:\MaoDou\geoDataProject\AI\city_data_six.json'
with open(file_path_six, 'r', encoding='utf-8') as f:
    city_data_six = json.load(f)

city_values_six = [(city['name'], city['value']) for city in city_data_six]

valid_city_values_six = []
for name, value in city_values_six:
        valid_city_values_six.append((name, value))

# province
file_province_path = r'D:\MaoDou\geoDataProject\AI\province_data.json'
with open(file_province_path, 'r', encoding='utf-8') as f:
    province_data = json.load(f)

province_values = [(province['name'], province['value']) for province in province_data]

valid_province_values = []
for name, value in province_values:
    valid_province_values.append((name, value))



# 海外

# # AI
locations = [
    {"name": "格鲁斯特大学", "coords": [-2.2386, 51.8683]},  # 英国，格鲁斯特
    {"name": "新加坡国立大学", "coords": [103.7764, 1.2966]},  # 新加坡
    {"name": "电子科技大学", "coords": [104.0685, 30.5711]},  # 中国，成都
    {"name": "阿尔伯特大学", "coords": [-113.4911, 53.5232]},  # 加拿大，埃德蒙顿
    {"name": "南洋理工大学", "coords": [103.6847, 1.3481]},  # 新加坡
    {"name": "下北泽大学", "coords": [139.6561, 35.6654]},  # 日本，下北泽
    {"name": "威斯康星麦迪逊", "coords": [-89.4012, 43.0731]},  # 美国，威斯康星
    {"name": "音乃木坂学院", "coords": [139.7033, 35.6604]},  # 日本，音乃木坂
    {"name": "伊利诺伊大学厄巴纳-香槟分校", "coords": [-88.2272, 40.1107]},  # 美国，香槟
    {"name": "慕尼黑大学", "coords": [11.5776, 48.1504]},  # 德国，慕尼黑
    {"name": "中国科学技术大学", "coords": [117.2830, 31.8611]},  # 中国，合肥
    {"name": "university of Bologna", "coords": [11.3545, 44.4949]},  # 意大利，博洛尼亚
    {"name": "University of Washington", "coords": [-122.3035, 47.6553]},  # 美国，西雅图
    {"name": "马里兰大学", "coords": [-76.9431, 38.9860]},  # 美国，马里兰
    {"name": "悉尼大学", "coords": [151.2111, -33.8887]},  # 澳大利亚，悉尼
    {"name": "Monash University", "coords": [145.1327, -37.8767]},  # 澳大利亚，墨尔本
    {"name": "兰州理工大学", "coords": [103.8323, 35.9053]},  # 中国，兰州
    {"name": "得克萨斯大学阿灵顿分校", "coords": [-97.1081, 32.7305]},  # 美国，阿灵顿
    {"name": "成均馆大学", "coords": [126.9768, 37.5663]},  # 韩国，首尔
    {"name": "曼彻斯特大学", "coords": [-2.2382, 53.4668]},  # 英国，曼彻斯特
    {"name": "英国东伦敦大学", "coords": [0.0169, 51.5106]},  # 英国，东伦敦
    {"name": "庆北大学", "coords": [129.0533, 35.8729]},  # 韩国，庆州
    {"name": "纽约大学", "coords": [-73.9964, 40.7306]},  # 美国，纽约
    {"name": "伦敦大学学院", "coords": [-0.1419, 51.5246]},  # 英国，伦敦
    {"name": "Paris Saclay", "coords": [2.1553, 48.7119]},  # 法国，巴黎
    {"name": "上海科技大学", "coords": [121.4744, 31.2090]},  # 中国，上海
    {"name": "亚利桑那州立大学", "coords": [-111.9339, 33.4167]},  # 美国，亚利桑那
    {"name": "布朗大学", "coords": [-71.4025, 41.8268]},  # 美国，罗德岛
    {"name": "the university of Cambridge", "coords": [0.1218, 52.2053]},  # 英国，剑桥
    {"name": "ESCP商学院", "coords": [2.3167, 48.8495]},  # 法国，巴黎
    {"name": "厦门大学马来西亚分校", "coords": [103.6631, 1.4940]},  # 马来西亚，吉隆坡
    {"name": "东京大学", "coords": [139.7454, 35.7116]},  # 日本，东京
    {"name": "Queen's University", "coords": [-75.6757, 44.2247]},  # 加拿大，金斯顿
    {"name": "Washington University in Saint Louis", "coords": [-90.3084, 38.6484]},  # 美国，圣路易斯
    {"name": "新南威尔士大学", "coords": [151.2400, -33.9170]},  # 澳大利亚，悉尼
    {"name": "维捷布斯克国立工艺大学", "coords": [30.3705, 55.1905]},  # 白俄罗斯，维捷布斯克
    {"name": "Kennesaw state university", "coords": [-84.6532, 34.0321]},  # 美国，肯尼斯索
    {"name": "中州奇士府", "coords": [113.3913, 34.8273]},  # 中国，中州
    {"name": "杜伦大学", "coords": [-1.5767, 54.7761]},  # 英国，杜伦
    {"name": "山东大学", "coords": [117.0191, 36.6828]},  # 中国，济南
    {"name": "马来亚大学", "coords": [101.7091, 3.1196]},  # 马来西亚，吉隆坡
    {"name": "代尔夫特理工大学", "coords": [4.3705, 52.0116]},  # 荷兰，代尔夫特
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
    symbol_size=5,  # 根据学员数量调整点的大小
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
        title="大模型与人工智能系统训练营\n      学员地理位置分布图",
        subtitle="报名人数：3218 人\n来自高校：802 所\n来自城市：221 个",
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

geo.render(r'D:\MaoDou\geoDataProject\AI\AI_world_map.html')
