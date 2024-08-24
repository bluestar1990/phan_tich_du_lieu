import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from IPython.display import Image

# Tải tập dữ liệu
df = pd.read_csv("Software_Professional_Salaries.csv")
print(df.head())

# Đếm số lượng công việc ở mỗi location
location_counts = df['Location'].value_counts()

# Tạo barplot cho số lượng công việc ở mỗi location
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Vẽ Barplot cho location và số lượng công việc
sns.barplot(x=location_counts.index, y=location_counts.values, palette="Set3")

# Xoay nhãn trục X để dễ đọc hơn nếu tên location dài
plt.xticks(rotation=90)

# Thêm tiêu đề và nhãn trục
plt.title("Số Lượng Công Việc Theo Location")
plt.xlabel("Location")
plt.ylabel("Số Lượng Công Việc")

plt.show()