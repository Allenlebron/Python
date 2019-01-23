import pandas as pds
df = pds.DataFrame([
        ("ZhangFei",32,75,100, 90),
        ("GuanYu",24,85,96,88.5),
        ("ZhaoYun",28,85,92,96.5),
        ("HuangZhong",29,65,85,100)],
    columns = ['name', 'age', 'chinese', 'math', 'english'])
print(df)
df.info()
print(df.columns)
for col in ['age', 'chinese', 'math', 'english']:
    print(col, df[col].mean())