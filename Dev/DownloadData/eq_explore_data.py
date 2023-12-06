from pathlib import Path
import json

# 将数据作为字符串读取并转换为Python对象
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 将数据文件转换为更易于阅读的版本
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)  # 缩进4
# path.write_text(readable_contents)

# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']

# 提取信息
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # 震级
    title = eq_dict['properties']['title']  # 标题
    lon = eq_dict['geometry']['coordinates'][0]  # 经度
    lat = eq_dict['geometry']['coordinates'][1]  # 纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
