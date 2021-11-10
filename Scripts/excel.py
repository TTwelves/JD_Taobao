'''
# @Title:
# @Time : 2021/11/4 12:06
# @File : excel.py
# @Software: PyCharm

'''
# 创建新的workbook（其实就是创建新的excel）
import xlwt
import yaml

with open('./demo2.yaml', 'r', encoding='utf-8') as f:
    datas = yaml.safe_load(f)


workbook = xlwt.Workbook(encoding='ascii')
# 创建新的sheet表
worksheet = workbook.add_sheet("京东-狗零食")

# 初始化样式
style = xlwt.XFStyle()

# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'  # 字体
font.bold = True  # 加粗
font.underline = True  # 下划线
font.italic = True  # 斜体

# 设置样式
style.font = font

# 往表格写入内容
worksheet.write(0, 0, "标题")
worksheet.write(0, 1, "价格")
worksheet.write(0, 2, "评价数")
worksheet.write(0, 3, "店铺名称")
worksheet.write(0, 4, "标签")
worksheet.write(0, 5, "链接")

for i in range(len(datas)):
    data = datas[i]
    worksheet.write(i+1, 0, data[2])
    worksheet.write(i+1, 1, data[0])
    worksheet.write(i+1, 2, data[1])
    worksheet.write(i+1, 3, data[3])
    worksheet.write(i+1, 4, data[4])
    worksheet.write(i+1, 5, data[5])

# 保存
workbook.save("京东-狗零食.xls")