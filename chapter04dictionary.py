d1 = {}
#print(d1['name'])  #报错：KeyError: 'name'
print(d1.get('name'))   #None
print(d1.get('name','default value of None value')) #default value of None value
d1.setdefault('name','default_value')   #如果'name'键不存在则添加
print(d1)

d2 = {'name':'ben','phone':13000000000}
print('name' in d2)