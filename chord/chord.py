from d3blocks import D3Blocks
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import webbrowser

df = pd.read_csv(r"C:\Users\amber\Documents\WeChat Files\wxid_kn5negt0o3h222\FileStorage\File\2024-07\chord.csv", usecols=[0, 1, 2])
df.columns = ['target', 'weight', 'source']
df = df.iloc[1:]
d3 = D3Blocks()
output_file = os.path.join(os.getenv('TEMP'), 'd3blocks', 'chord.html')

# 生成弦图
d3.chord(df)


# 生成弦图，并保存到指定路径
# if os.path.exists(output_file):
#     # 读取 HTML 文件内容
#     with open(output_file, 'r', encoding='utf-8') as file:
#         html_content = file.read()
#
#     # 打印生成的 HTML 内容（用于调试）
#     print(html_content)
#
#     # 查找特定的 <path> 元素，通过 title 来识别
#     pattern = r'(<path[^>]*><title>Guangxi\s*→\s*Guangxi\s*1\.111167454<\/title><\/path>)'
#     match = re.search(pattern, html_content)
#
#     if match:
#         path_element = match.group(1)
#         # 生成新的 <text> 元素，您可以根据需要调整位置和样式
#         text_element = '<text x="300" y="300" fill="red" font-size="12">1.111167454</text>'
#         # 在匹配到的 <path> 元素后面添加 <text> 元素
#         modified_html_content = html_content.replace(path_element, path_element + text_element)
#
#         # 将修改后的内容写回 HTML 文件
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(modified_html_content)
#
#         # 打开浏览器显示修改后的 HTML 文件
#         webbrowser.open(output_file)
#     else:
#         print("未找到匹配的 <path> 元素")
# else:
#     print(f"文件 {output_file} 未生成")