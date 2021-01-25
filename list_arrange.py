# python3で必ず実行する！ python2だとencodingがエラーになるので注意！
with open('./item_list.csv',encoding='utf-8') as f:
	list = []
	for row in f:
		row = row.rstrip().split(',')
		list.append(row)
print(list)