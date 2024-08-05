from pathlib import Path
import json
import matplotlib.pyplot as plt
import pandas as pd

out_data = {
    '名称': [],
    '位置': [],
    '时间': [],
    '季节': [],
    '天气': [],
    '用途': []
}


def draw_table(out_data):
    # 创建数据字典
    plt.rcParams['font.family'] = 'SimHei'

    # 创建 DataFrame
    df = pd.DataFrame(out_data)

    # 创建图形
    fig, ax = plt.subplots(figsize=(12, 5))  # 调整图形的大小
    ax.axis('tight')
    ax.axis('off')

    # 创建表格
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center')

    # 创建表格
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center',
                    colColours=['#f5f5f5']*len(df.columns))

    # 设置表格字体大小和字体
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for key, cell in table._cells.items():
        cell.set_height(0.1)
        cell.set_edgecolor('black')
        cell.set_facecolor('#e6f7ff')  # 设置背景颜色
        if key[0] == 0:
            cell.set_facecolor('#897689')

    # 设置标题
    plt.title('钓鱼参考', fontsize=15, color='black', pad=10)

    # 调整列宽
    table.auto_set_column_width(range(len(out_data)))  # 调整列宽，使内容适合

    plt.show()

if __name__ == '__main__':

    with open('./stardewwiki/temp/results.json', encoding='utf-8') as f:
        raw_data = json.load(f)

    for fish in raw_data:
        if '春季' in fish['季节'] and '收集包' in fish['用途']:
            out_data['名称'].append(fish['名称'])
            out_data['位置'].append(fish['位置'])
            out_data['时间'].append(fish['时间'])
            out_data['季节'].append(fish['季节'])
            out_data['天气'].append(fish['天气'])
            out_data['用途'].append(fish['用途'])

    draw_table(out_data)