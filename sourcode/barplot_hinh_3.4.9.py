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
# Tạo barplot để thể hiện lương trung bình tại mỗi location, nằm ngang
plt.figure(figsize=(12, 8))  # Điều chỉnh kích thước biểu đồ

# Sử dụng barplot với orientation nằm ngang
sns.set(style="whitegrid")
sns.barplot(x="Salary", y="Location", data=df, palette="Set3", orient="h")

# Thêm tiêu đề và nhãn trục
plt.title("Lương Trung Bình Theo Location")
plt.xlabel("Lương")
plt.ylabel("Location")

# Hiển thị biểu đồ
plt.show()