import openpyxl
#打开工作簿
workbook=openpyxl.load_workbook("景区天气.xlsx")
#选择要操作的工作表
sheet=workbook["景区天气"]
#表格数据是二维列表，先便利的是行，后遍历的是列
lst=[] #储存的是行数据
for row in sheet.rows:
    sublst=[] #储存单元格数据
    for cell in row:  #cell单元格
        sublst.append(cell.value)
    lst.append(sublst)
for item in lst:
    print(item)