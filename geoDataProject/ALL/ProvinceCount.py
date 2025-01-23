#统计每个省的学员数量

import pandas as pd
import json
# 转为json

# 读取Excel文件
df = pd.read_excel('训练营平台用户表-14800人.xlsx')

# 分割地址列，提取省和市
df[['省份', '城市']] = df['城市'].str.split('/', expand=True)


# 如果省份是“香港特别行政区”，则城市名称改为“香港”
df['省份'] = df['省份'].where(df['省份'] != '香港特别行政区', '香港')

# 统计每个城市的学员数量
city_counts = df['省份'].value_counts().reset_index()
city_counts.columns = ['省份', '学员数量']

# 将城市数量转换为字典格式，准备 ECharts 数据
data = []
for index, row in city_counts.iterrows():
    data.append({"name": row['省份'], "value": row['学员数量']})

# 将数据输出为 JSON 格式，并保存到文件
with open('province_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("数据统计完成，并已保存至 province_data.json 文件。")