import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 读取江苏省的 GeoJSON 文件
gdf = gpd.read_file('江苏省.json')

# 创建接待游客量的数据框
data = {
    'city': ['南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', 
             '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', 
             '泰州市', '宿迁市'],
    'tourist_visitors': [1543.8, 370, 675, 559.6, 1285.6, 653.87, 679.15, 
                         637.21, 668.54, 800, 515.3, 526.34, 174.36]
}
data_df = pd.DataFrame(data)

# 合并 GeoDataFrame 和游客量数据框
gdf = gdf.merge(data_df, left_on='name', right_on='city', how='left')

# 检查合并结果
print(gdf[['name', 'tourist_visitors']].head())

# 检查缺失值
print(gdf['tourist_visitors'].isnull().sum())

# 填充缺失值
gdf = gdf.assign(tourist_visitors=gdf['tourist_visitors'].fillna(0))

# 绘制热力图
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
gdf.boundary.plot(ax=ax, linewidth=1)  # 绘制边界
gdf.plot(column='tourist_visitors', ax=ax, legend=True,
         legend_kwds={'label': "Number of Tourists (in 10,000)",
                      'orientation': "horizontal"},
         cmap='OrRd')

# 添加标题
ax.set_title('2024 Tourist Visitors in Jiangsu Province', fontdict={'fontsize': '15', 'fontweight': '3'})

# 显示图形
plt.show()
