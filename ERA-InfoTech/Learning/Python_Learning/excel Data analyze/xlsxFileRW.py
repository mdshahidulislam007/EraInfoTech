import xlrd

file_location = "C:/Users/palas/PycharmProjects/Python_learning/UEC 14.09.15 (11).xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
for col in range(sheet.nrows):
    print(sheet.cell_value(1,col))