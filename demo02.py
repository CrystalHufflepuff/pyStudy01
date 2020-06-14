'''
#元组 不能修改是元组的优点和特点
a=(1,2,3,4,"雷狮","帕洛斯",True,False)
print(a[4],a[5])
print(a.index("雷狮"))  #查找某个值的下标 index中只能输入一个值
print(a.count("帕洛斯")) #统计某个值的数量
print(a[-1])
#下标还可以倒着数，从后往前-1 -2 -3……
#二维元组
b=(a,"佩利","卡米尔") #这种情况下元组内有三个值
print(b[1],b[0][4])
#切片：批量取值 属性：左闭右开
print(a[4:7])
'''
'''
#数组 元组写好后不能修改，数组可以修改
c=[1,2,3,4,"雷狮","帕洛斯",True,False]

print(c[5])
c.append("捕树菇地龙树")#append 插入的数据永远在数组最后一位
print(c)
c.insert(4,"Ray")
print(c)
#c.pop(4)#剪切，将数组中某个字剪切掉

d=c.pop(4)
print(c)
print(d)
a1=c.pop(0)
a2=c.pop((0))
print(a1+a2)
print(a1)
print(a2)
xx=["你好","好久不见"]
c.extend(xx)
print(c)

c.remove(2) #remove 传的不是下标，而是一个固定值，把某个值在数组中删除
print(c)
#注意下标不能越界
#元组、数组、字典的定义分别是()[]{}，但是取某个元素时依然是a[5]这样的格式
'''

#字典
'''
字典中的值没有顺序
字典的结构是键值对的结构 key:value
字符串都要加引号

d={
    "name":"张三",
    0:"haha",
    "age":25
}
#字典的取值
print(d["name"])#取值：中括号里是key值
#字典的新增
d["high"]="183cm"
print(d)
#字典的修改
d["name"]="lisi"
print (d)

d1=d.get("age")
print(d1)
d2=d.pop("high")
print(d2)
print(d)
d.update(name=1111)#新增或修改
print(d)'''

'''
#对比print(d.get("name"))和print(d["name"])
#下标正确时没有区别，下标不正确时，get函数返回值为空，数组取下标则报错
print(d.get("name"))
print(d["name"])
print(d.get("name1"))
print(d["name1"])
'''
'''
#通用删除 但不适用于元组，因为元组不呢能修改
c=[1,2,3,4,"雷狮","帕洛斯",True,False]
del d[0]#注意字典中的“下标”全都是指key的值
print(d)
del c[2]
print(c)
'''
#练习：获取用户的个人信息并存储到字典中
print("请输入用户的个人信息：")
n=input("输入姓名：")
a=input("输入年龄：")
s=input("输入性别：")
Mess={"name":n,"age":a,"sex":s}
print(Mess)