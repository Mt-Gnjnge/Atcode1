import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

df_age = pd.read_csv("Population_Pillamid.csv")
print(df_age.columns)

sns.set(style='whitegrid')
fig, ax = plt.subplots(figsize=(7, 5),dpi=100)
plt.subplots_adjust(left=0.2, right=0.85, bottom=0.05, top=1.0)

df_age["man"] *= -1

age_colors = ["#406c93", "#d94448"]
age_names = ["man", "woman"]

for name, color in zip(age_names, age_colors):
    sns.barplot(x=name, y=df_age.index, data=df_age, color=color, label=name,
                orient='h', order=df_age.index, ax=ax)

ax.set_xlabel("")
ax.set_ylabel("age", fontsize=12)
ax.set_xlim(-1000, 1000)

label = [1000, 750, 500, 250, 0, -250, -500, -750, -1000]

ax.set_xticks(label)  # 正しい目盛り位置を設定
ax.set_xticklabels([str(abs(x)) for x in label])  # 正の値を表示するために絶対値を使用


ax.legend(loc='lower left')

plt.savefig('graph.png')
plt.show(block=False)
# time.sleep(5)
plt.pause(3)
plt.close()