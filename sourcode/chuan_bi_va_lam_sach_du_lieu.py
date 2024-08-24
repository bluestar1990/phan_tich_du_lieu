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

print("========================# Shape of data=================")
print(df.shape)

print("========================# Hiển thị tất cả cột=================")
print(df.columns)

print("========================# Hiện thị thông tin bộ dữ liệu=================")
print(df.info)

print("========================# Kiểm tra giá trị null trong bộ dữ liệu=================")
print(df.isnull().sum())

print("========================# Hiển thị tất cả Location trong bộ dữ liệu=================")
print(df["Location"].unique())

print("========================Kiểm tra Trung bình, Trung vị, Tối đa và Tối thiểu của Lương========================")
print("Mean Salary:", round(df["Salary"].mean()))
print("Median Salary:", round(df["Salary"].median()))
print("Highest Salary:", round(df["Salary"].max()))
print("Lowest Salary:", round(df["Salary"].min()))



