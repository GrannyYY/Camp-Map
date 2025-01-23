# 画中国地区学员分布

import json
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

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



# 海外
# all
locations = [
    {"name": "Trinity College Dublin", "coords": [-6.2546, 53.3430]},  # Dublin, Ireland
    {"name": "Shandong University", "coords": [117.1305, 36.6628]},  # Jinan, China
    {"name": "诺丁汉大学", "coords": [-1.2253, 52.9548]},  # Nottingham, UK
    {"name": "Friedrich-Alexander-Universität Erlangen-Nürnberg", "coords": [11.0061, 49.4780]},  # Erlangen, Germany
    {"name": "京都大学", "coords": [135.784, 35.0268]},  # Kyoto, Japan
    {"name": "NC State University", "coords": [-78.6749, 35.7845]},  # Raleigh, USA
    {"name": "INSA", "coords": [4.8282, 45.7821]},  # Lyon, France
    {"name": "山东外国语职业技术大学", "coords": [119.4612, 36.7069]},  # Shandong, China
    {"name": "都柏林三一学院", "coords": [-6.2535, 53.3438]},  # Dublin, Ireland
    {"name": "Eurecom", "coords": [7.0147, 43.6067]},  # Sophia Antipolis, France
    {"name": "西安电子科技大学", "coords": [108.9202, 34.2301]},  # Xi'an, China
    {"name": "University of Tartu", "coords": [26.7277, 58.3784]},  # Tartu, Estonia
    {"name": "湘潭大学", "coords": [112.9355, 27.8578]},  # Xiangtan, China
    {"name": "KIT", "coords": [8.4035, 48.6642]},  # Karlsruhe, Germany
    {"name": "UoG", "coords": [-2.243, 53.2985]},  # Glasgow, UK
    {"name": "新加坡国立大学", "coords": [103.7764, 1.2957]},  # Singapore
    {"name": "电子科技大学", "coords": [104.0743, 30.6644]},  # Chengdu, China
    {"name": "中国科学院大学", "coords": [116.3241, 39.9825]},  # Beijing, China
    {"name": "阿尔伯特大学", "coords": [-113.5254, 53.5232]},  # Edmonton, Canada
    {"name": "南洋理工大学", "coords": [103.6813, 1.3481]},  # Singapore
    {"name": "下北泽大学", "coords": [139.6542, 35.6623]},  # Tokyo, Japan
    {"name": "威斯康星麦迪逊", "coords": [-89.4037, 43.0731]},  # Madison, USA
    {"name": "音乃木坂学院", "coords": [139.665, 35.6418]},  # Tokyo, Japan
    {"name": "UIUC", "coords": [-88.2242, 40.1107]},  # Urbana-Champaign, USA
    {"name": "中国科学技术大学", "coords": [117.236, 31.8106]},  # Hefei, China
    {"name": "university of Bologna", "coords": [11.3543, 44.4937]},  # Bologna, Italy
    {"name": "University of Washington", "coords": [-122.3050, 47.6553]},  # Seattle, USA
    {"name": "马里兰大学", "coords": [-76.9406, 39.0007]},  # College Park, USA
    {"name": "悉尼大学", "coords": [151.2093, -33.8688]},  # Sydney, Australia
    {"name": "Monash University", "coords": [145.1327, -37.8978]},  # Melbourne, Australia
    {"name": "uta", "coords": [-97.1182, 32.7357]},  # Arlington, USA
    {"name": "Imperial College London", "coords": [-0.1754, 51.4980]},  # London, UK
    {"name": "成均馆大学", "coords": [126.9783, 37.5117]},  # Seoul, South Korea
    {"name": "曼彻斯特大学", "coords": [-2.2380, 53.4808]},  # Manchester, UK
    {"name": "英国东伦敦大学", "coords": [0.0085, 51.5149]},  # London, UK
    {"name": "庆北大学", "coords": [129.0837, 35.8705]},  # Gyeongju, South Korea
    {"name": "纽约大学", "coords": [-73.9965, 40.7306]},  # New York City, USA
    {"name": "伦敦大学学院", "coords": [-0.1321, 51.5246]},  # London, UK
    {"name": "Paris Saclay", "coords": [2.2261, 48.7141]},  # Paris, France
    {"name": "慕尼黑大学", "coords": [11.5820, 48.1459]},  # Munich, Germany
    {"name": "多伦多大学", "coords": [-79.3950, 43.6629]},  # Toronto, Canada
    {"name": "上海科技大学", "coords": [121.5957, 31.1991]},  # Shanghai, China
    {"name": "the university of Cambridge", "coords": [0.1218, 52.2053]},  # Cambridge, UK
    {"name": "ESCP商学院", "coords": [2.3341, 48.8574]},  # Paris, France
    {"name": "厦门大学马来西亚分校", "coords": [103.6336, 1.3231]},  # Johor, Malaysia
    {"name": "东京大学", "coords": [139.7271, 35.6829]},  # Tokyo, Japan
    {"name": "Queen's University", "coords": [-5.9304, 54.5984]},  # Belfast, UK
    {"name": "新南威尔士大学", "coords": [151.2000, -33.8939]},  # Sydney, Australia
    {"name": "维捷布斯克国立工艺大学", "coords": [30.9375, 55.1944]},  # Vitebsk, Belarus
    {"name": "Kennesaw state university", "coords": [-84.6160, 34.0282]},  # Kennesaw, USA
    {"name": "middlebury institute of international studies", "coords": [-122.6443, 36.5953]},  # Monterey, USA
    {"name": "墨尔本大学", "coords": [144.9631, -37.8136]},  # Melbourne, Australia
    {"name": "佐治亚理工学院", "coords": [-84.3963, 33.7741]},  # Atlanta, USA
    {"name": "韩国延世大学", "coords": [126.9385, 37.5667]},  # Seoul, South Korea
    {"name": "Johannes Kepler University Linz", "coords": [14.2966, 48.3032]},  # Linz, Austria
    {"name": "奥克兰大学", "coords": [174.7633, -36.8485]},  # Auckland, New Zealand
    {"name": "University College London", "coords": [-0.1322, 51.5246]},  # London, UK
    {"name": "UMich", "coords": [-83.7382, 42.2780]},  # Ann Arbor, USA
    {"name": "Wellesley College", "coords": [-71.2973, 42.2923]},  # Wellesley, USA
    {"name": "巴黎综合理工", "coords": [2.2454, 48.7164]},  # Paris, France
    {"name": "gatech", "coords": [-84.3963, 33.7741]},  # Atlanta, USA
    {"name": "杜伦大学", "coords": [-1.5744, 54.7743]},  # Durham, UK
    {"name": "墨尔本大学", "coords": [144.9631, -37.8136]},  # Melbourne, Australia
    {"name": "悉尼大学", "coords": [151.2093, -33.8688]},  # Sydney, Australia
    {"name": "马来亚大学", "coords": [101.6810, 3.1206]},  # Kuala Lumpur, Malaysia
    {"name": "NAU is not A Univ", "coords": [105.9505, 35.4839]},  # Flagstaff, USA
    {"name": "KTH Royal Institute of Technology", "coords": [18.0701, 59.3748]},  # Stockholm, Sweden
    {"name": "Singapore Management University", "coords": [103.8480, 1.2962]},  # Singapore
    {"name": "北京邮电大学", "coords": [116.3145, 39.9839]},  # Beijing, China
    {"name": "长沙理工大学", "coords": [113.0045, 28.2434]},  # Changsha, China
    {"name": "中州奇士府", "coords": [113.6247, 34.7481]},  # Zhengzhou, China
    {"name": "武汉大学", "coords": [114.3690, 30.5421]},  # Wuhan, China
    {"name": "Monash University", "coords": [145.1327, -37.8978]},  # Melbourne, Australia
    {"name": "politecnico di torino", "coords": [7.6481, 45.0704]},  # Turin, Italy
    {"name": "厦门大学马来西亚分校", "coords": [103.6336, 1.3231]},  # Johor, Malaysia
    {"name": "新加坡国立大学", "coords": [103.7764, 1.2957]},  # Singapore
    {"name": "ucsc", "coords": [-122.0662, 36.9989]},  # Santa Cruz, USA
    {"name": "University of Wisconsin, Madison", "coords": [-89.4037, 43.0731]},  # Madison, USA
    {"name": "里贾纳大学", "coords": [-104.6174, 52.1332]},  # Regina, Canada
    {"name": "清华大学", "coords": [116.3271, 39.9610]},  # Beijing, China
    {"name": "Monash University", "coords": [145.1327, -37.8978]},  # Melbourne, Australia
    {"name": "Northwestern University", "coords": [-87.6278, 42.0516]},  # Evanston, USA
    {"name": "清华大学", "coords": [116.3271, 39.9610]},  # Beijing, China
    {"name": "Northeastern University", "coords": [-71.0892, 42.3400]},  # Boston, USA
    {"name": "伦斯勒理工", "coords": [-73.6781, 42.7307]},  # Troy, USA
    {"name": "大连理工大学城市学院", "coords": [121.6195, 38.9153]},  # Dalian, China
    {"name": "新南威尔士大学", "coords": [151.2000, -33.8939]},  # Sydney, Australia
    {"name": "University of Washington", "coords": [-122.3050, 47.6553]},  # Seattle, USA
    {"name": "Duke University", "coords": [-78.9382, 36.0014]},  # Durham, USA
    {"name": "悉尼大学", "coords": [151.2093, -33.8688]},  # Sydney, Australia
    {"name": "佐治亚理工学院", "coords": [-84.3963, 33.7741]},  # Atlanta, USA
    {"name": "伊利诺伊理工", "coords": [-87.6278, 41.8341]},  # Chicago, USA
    {"name": "代尔夫特理工大学", "coords": [4.5764, 52.0116]},  # Delft, Netherlands
    {"name": "澳大利亚国立大学", "coords": [149.1165, -35.2809]},  # Canberra, Australia
    {"name": "斯坦福大学", "coords": [-122.1697, 37.4275]},  # Stanford, USA
    {"name": "卡耐基梅隆大学", "coords": [-79.9445, 40.4440]},  # Pittsburgh, USA
    {"name": "悉尼大学", "coords": [151.2093, -33.8688]},  # Sydney, Australia
    {"name": "佐治亚理工学院", "coords": [-84.3963, 33.7741]},  # Atlanta, USA
    {"name": "法政大学", "coords": [139.4527, 35.6967]},  # Tokyo, Japan
    {"name": "南开大学", "coords": [117.1812, 39.1040]},  # Tianjin, China
    {"name": "asu", "coords": [-111.9331, 33.4168]},  # Tempe, USA
    {"name": "HIT", "coords": [126.6634, 45.7464]},  # Harbin, China
    {"name": "西九州大学", "coords": [129.7383, 33.1164]},  # Nagasaki, Japan
    {"name": "University of Wollongong", "coords": [150.8667, -34.4237]},  # Wollongong, Australia
    {"name": "亚马逊日本", "coords": [139.6955, 35.6895]},  # Tokyo, Japan
    {"name": "Washington University in Saint Louis", "coords": [-90.3052, 38.6489]},  # St. Louis, USA
    {"name": "Indiana University", "coords": [-86.5260, 39.1723]},  # Bloomington, USA
    {"name": "燕山大学", "coords": [114.4909, 40.2736]},  # Qinhuangdao, China
    {"name": "杜克大学", "coords": [-78.9382, 36.0014]},  # Durham, USA
    {"name": "北京大学", "coords": [116.3062, 39.9995]},  # Beijing, China
    {"name": "Psu", "coords": [-77.0522, 40.7952]},  # State College, USA
    {"name": "重庆大学", "coords": [106.5469, 29.5481]},  # Chongqing, China
    {"name": "University of Southern California", "coords": [-118.2890, 34.0226]},  # Los Angeles, USA
    {"name": "墨尔本大学", "coords": [144.9631, -37.8136]},  # Melbourne, Australia
    {"name": "University of Suffolk", "coords": [1.1561, 52.0537]},  # Ipswich, UK
    {"name": "uiuc", "coords": [-88.2242, 40.1107]},  # Urbana-Champaign, USA
    {"name": "布朗大学", "coords": [-71.4025, 41.8268]},  # Providence, USA
    {"name": "巴特雷特大学", "coords": [-0.1276, 51.4642]},  # London, UK
    {"name": "CUHK", "coords": [114.1975, 22.3964]},  # Hong Kong
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
        title="训练营平台用户地理位置分布图",
        subtitle="报名人数：14720 人\n来自高校：1990 所\n来自城市：451 个",  # 添加副标题
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

geo.render(r'D:\MaoDou\geoDataProject\ALL\All_world_map.html')
