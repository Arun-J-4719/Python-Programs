import xlrd
location="/home/administrator/Desktop/Arun/Data.xlsx"
workbook=xlrd.open_workbook(location)
print "File Opened..."
sheet=workbook.sheet_by_index(0)
print "Index Selected..."
print "Excel Data Are Retrieved..."
data=[[sheet.cell_value(c,r) for r in range(sheet.nrows)]for c in range(sheet.ncols)]
print "Retrived Data Are:"
for i in data:
	print i