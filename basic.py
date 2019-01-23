import time;
# 输入输出
# name = input("what's your name?")
name = '什么鬼'
sum = 100 + 200
print('hello,%s' %name)
print('sum= %d' %sum)
print('当前时间戳：',time.time())
print('格式化时间：',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#if...else条件语句
name = 80
if name >=90:
    print('excellent!')
else:
    if name < 60:
        print('fail')
    else:
            print('Good job')
#for循环
# 1+3+5...99
sum = 0
for number in range(1,100,2):
    sum = sum + number
print(sum)

#while循环
number = 1
sum = 0
while number < 100:
    sum = sum + number
    number = number + 2
print(sum)

#数据类型：列表，元组，字典，集合
## 列表
lists = ['a','b','c']
# 追加
lists.append('d')
# 长度
print(len(lists))
# 插入
lists.insert(0,'a')
# 删除最后一个元素
lists.pop()
# 输出
print(lists)

##元组:tuple
tuples =('A','B')
print(tuples[1])

## 字典:dictionary
score ={'james':99,'wade':96,'kobe':98}
# 添加一个元素
score['paul']=95
# 删除一个元素
score.pop('kobe')
# 查找一个key对应的值
print(score.get('wade'))
# 判断元素是否存在
print('james' in score)
# 不存在默认一个值
print(score.get('iverson',99))
print(score)

## 集合：set
s= set(['张三','李四','王五'])
s.add('王二麻子')
s.remove('张三')
print(s)
print('王五' in s)

## 函数
def addNumber(number):
    return number + 1
print(addNumber(99))

# A + B
# for循环
sum = 0
for x in input().split():
    sum = sum + int(x)
print(sum)

# while循环
while True:
       try:
              line = input()
              a = line.split()
              print(int(a[0]) + int(a[1]))
       except:
              break
# while循环和for结合
result = 0
while True:
        try:
            for x in input().split():
                result = result + int(x)
            print(result)
        except:
               break

