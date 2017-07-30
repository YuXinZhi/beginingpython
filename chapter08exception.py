

def descriptionperson(pserson):
    '''
    #person['name']的值不存在时，'name = '会被输出
    '''
    print('name = ' + pserson['name'])
    print('sex = ' + pserson['sex'])


def descriptionperson1(pserson):
    print('name1 = ',pserson['name'])
    try:
        print('sex = ' , pserson['sex'])
    except KeyError:
        pass

person = {'name':'ben'}
person1 = {'sex = ':'男'}

descriptionperson1(person1)
#descriptionperson1(person)