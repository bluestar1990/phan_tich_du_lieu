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
# Đặt số lượng bins
n_bins = 20

# Tạo biểu đồ histogram với 20 bins
plt.figure(figsize=(20, 5))
df["Rating"].hist(bins=n_bins)

# Thêm tiêu đề và nhãn trục
plt.title("Phân Phối Company Rating")
plt.xlabel("Rating")
plt.ylabel("Số Lượng Công Ty")

# Hiển thị biểu đồ
plt.show()