# excel转为json

import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('data.xlsx')


# 分割地址列，提取省和市
df[['省份', '城市']] = df['城市'].str.split('/', expand=True)

# 处理市辖区的情况，如果城市名称是“市辖区”，则用前面的市名称代替
# 这里使用 `where` 方法进行条件替换
df['城市'] = df['城市'].where(df['城市'] != '市辖区', df['省份'])
df['城市'] = df['城市'].where(df['城市'] != '省直辖县级行政区划', df['省份'])
df['城市'] = df['城市'].where(df['城市'] != '自治区直辖县级行政区划', df['省份'])

# 如果省份是“香港特别行政区”，则城市名称改为“香港”
df['城市'] = df['城市'].where(df['省份'] != '香港特别行政区', '香港')
df['城市'] = df['城市'].where(df['省份'] != '新疆维吾尔自治区', '新疆')

# 统计每个城市的学员数量
city_counts = df['城市'].value_counts().reset_index()
city_counts.columns = ['城市', '学员数量']

# 将城市数量转换为字典格式，准备 ECharts 数据
data = []
for index, row in city_counts.iterrows():
    data.append({"name": row['城市'], "value": row['学员数量']})

# 将数据输出为 JSON 格式，并保存到文件
with open('city_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("数据统计完成，并已保存至 city_data.json 文件。")