import numpy as np
import matplotlib.pyplot as plt

# 设置九个指标
labels = np.array(["指标1", "指标2", "指标3", "指标4", "指标5",
                   "指标6", "指标7", "指标8", "指标9"])
num_vars = len(labels)

# 指标值（示例数据）
values = np.array([80, 70, 85, 90, 75, 60, 95, 85, 70])

# 计算角度
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
values = np.concatenate((values, [values[0]]))  # 闭合雷达图
angles += angles[:1]  # 角度也需闭合

# 创建图形
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制雷达图
ax.fill(angles, values, color='b', alpha=0.25)  # 填充
ax.plot(angles, values, color='b', linewidth=2)  # 线条
ax.set_yticklabels([])  # 隐藏y轴标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# 显示图形
plt.title("九个指标的雷达图")
plt.show()
