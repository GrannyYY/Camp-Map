#分级城市数据实现点的大小不一
#rust

import json

file_path = r'D:\MaoDou\geoDataProject\Rust\city_data.json'
with open(file_path, 'r', encoding='utf-8') as f:
    city_data = json.load(f)


def classify_city(city):
    value = city['value']
    if value >= 200:
        return "city_data_one.json"
    elif value >= 100:
        return "city_data_two.json"
    elif value >= 50:
        return "city_data_three.json"
    elif value >= 20:
        return "city_data_four.json"
    elif value >= 3:
        return "city_data_five.json"
    else:
        return "city_data_six.json"

classified_data = {
    "city_data_one.json": [],
    "city_data_two.json": [],
    "city_data_three.json": [],
    "city_data_four.json": [],
    "city_data_five.json": [],
    "city_data_six.json": []
}

for city in city_data:
    file_name = classify_city(city)
    classified_data[file_name].append(city)

# 将分类结果写入文件
for file_name, data in classified_data.items():
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

print("数据分类完成，文件已生成！")