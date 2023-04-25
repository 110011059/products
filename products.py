produsts = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	produsts.append([name, price])
print(produsts)

produsts[0][0]