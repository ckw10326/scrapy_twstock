import twstock
twselist = []#上市代號
tpexliet = []#上櫃代號

for i in twstock.twse:
    if len(i) == 4:
        twselist.append(i)

for i in twstock.tpex:
    if len(i) == 4:
        tpexliet.append(i)

print("上市股票數量:",len(twselist))
for i in twselist:
    print(i)
print("上櫃股票數量:",len(tpexliet))
for i in tpexliet:
    print(i)

print("test2")